#! /usr/bin/perl

# ============================================================================
# $RCSfile$
# $Source$
# $Revision$
# $Date$
# $Author$
# $Name$
#
# DESCRIPTION:
# ============================================================================

# PRAGMAS
use strict;
use warnings;

# MODULES
use Getopt::Long;
use File::Spec;
use Data::Dumper;
use Readonly;
use Net::SFTP::Foreign;

# LIBRARIES

# ----------------------------------------------------------------------------

# Data::Dumper configuration
$Data::Dumper::Sortkeys = 1;
$Data::Dumper::Indent   = 1;

my (undef, undef, $app) = File::Spec->splitpath($0);

# SFTP account info
Readonly my $URL => 'ftp.gliders.ioos.us';
# Data provider user name: YOU MUST PROVIDE YOUR CREDENTIALS!
Readonly my $USER => 'USERNAME';
# Data provider password: YOU MUST PROVIDE YOUR CREDENTIALS!
Readonly my $PASS => 'PASSWORD';
Readonly my $PORT => 22;

my $BASE_REMOTE_DIR = './upload';

# Default options
my $VERBOSE; # Net::SFTP::Foreign debugging statements
my $DELETE; # Deletes each file on successful transfer
my $SOURCE_DIR; # Directory to search for NetCDF (.nc) files
my $REMOTE_DIR; # Remote destination directory

# Usage message
my $USAGE =<<"END_USAGE";
NAME
    $app - Secure FTP transfer of NetCDF files to IOOS NGDAC

SYNOPSIS
    $app --remote-dir DIRECTORY [--help] [--source-dir DIRECTORY] [--delete-on-success] 
        [ncfile1,ncfile2,...]

DESCRIPTION
    Upload NetCDF files to the IOOS National Glider Data Aggregation Center
    via secure ftp ($URL).  Individual files may be specified on the command 
    line.  Files are uploaded to the directory specified using the 
    --remote-dir option which, if it doesn't exist, is created under:

        $BASE_REMOTE_DIR

    Specifying a remote destination via the --remote-dir option is mandatory.

    --help
        Print help message and exit

    --remote-dir => MANDATORY
        Remote destination directory.  Specify the child directory under

            $BASE_REMOTE_DIR

    --source-dir
        Transfer all files contained in the specified directory    

    --delete-on-success
        Delete the local file copy on successful tranfer to the remote
        destination

END_USAGE

# Option processing
my $options_okay = GetOptions(
    'help'  => sub { print $USAGE; exit 0 },
    'verbose' => \$VERBOSE,
    'delete-on-success' => \$DELETE,
    'source-dir=s' => \$SOURCE_DIR,
    'remote-dir=s' => \$REMOTE_DIR,
);
!$options_okay and exit 1;

# User MUST specify a remote location
!$REMOTE_DIR and die "No remote destination specified";

my @in_files;
# Files can come from either, in this order of preference:
# 1. A directory specified by the --source-dir option
# 2. Individual files listed on the command line
if ($SOURCE_DIR) { # Check the option first
    ! -d $SOURCE_DIR && die "Invalid directory specified: $SOURCE_DIR";
    @in_files = glob "${SOURCE_DIR}/*.nc";
}
else { # Otherwise, see if a file(s) has been specified on the command line
	# Take the list of files either from the command line or from a pipe
	if (@ARGV) { # Files from the command line
	    @in_files = grep {-f} @ARGV;
	}
	elsif (-t) { # STDIN
	    print $USAGE;
	    exit 1;
	}
	else { # Pipe
	    @in_files = <>;
	    chomp @in_files;
	}
}

#$Data::Dumper::Varname = 'Selected Files';
#print Dumper(\@in_files);

# Keep only files ending in '.nc$'
my @nc_files = grep { /\.nc$/ } @in_files;
$Data::Dumper::Varname = 'NetCDF Files';
$VERBOSE and print Dumper(\@nc_files);
#exit 13;

!@nc_files and die "No files to sftp!";

# Connect to the remote server.  Set autodie => 1 to exit on failure
print "Connecting via SFTP: $URL..";
my $sftp = Net::SFTP::Foreign->new($URL,
    user => $USER,
    password => $PASS,
    port => $PORT);
$sftp->die_on_error("SSH Connection Failed!");
print "Connected\n";

# See if the remote destination exists
my $REMOTE_DEST = "${BASE_REMOTE_DIR}/${REMOTE_DIR}";
my $deployment_dir = $sftp->ls($REMOTE_DEST);
#$Data::Dumper::Varname = 'Remote Destination';
#print Dumper($deployment_dir);

# Create the remote directory if it doesn't already exist
if (!$deployment_dir) {
    print "Creating NEW remote destination: $REMOTE_DEST\n";
    my $success = $sftp->mkdir($REMOTE_DEST);
    !$success and die $sftp->error;
}

# Transfer each file
my $num_files = 0;
NC_FILE:
foreach my $local_nc (@nc_files) {

    # Create the fully-qualified remote file name
    my (undef, undef, $nc) = File::Spec->splitpath($local_nc);
    my $remote_nc = File::Spec->catfile($REMOTE_DEST, $nc);

    $VERBOSE and print "Transferring: $remote_nc\n";

    # Transfer the file
    my $success = $sftp->put($local_nc, $remote_nc);
    if (!$success) {
        warn "Failed transfer: $local_nc (" . $sftp->error . ")\n";
        next NC_FILE;
    }

    # Increment the file counter
    $num_files++;

    # Delete the file if specified via --delete-on-success
    if ($DELETE) {
        $VERBOSE and print "Deleting local copy: $local_nc\n";
        unlink $local_nc;
    }

}

print "${num_files}/" . scalar @nc_files . " successfully uploaded\n";
