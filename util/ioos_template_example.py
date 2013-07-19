# 2013 derrick.snowden@noaa.gov: initial version of python script for creating
#   IOOS glider NetCDF template.
# 2013-07-19 kerfoot@marine.rutgers.edu: modified script to adhere to most
#   recent version of CDL template:
#     - creation of variables and addition of recommended variable attributes
#     - variable attributes are added as dictionary items so that they can be
#       sorted and added alphabetically.
#
# Script to create example glider trajectory file.
# DIMENSIONS (SIZE):
#   trajectory: (1)
#   time: (unlim)
#   time_uv: (1)
# REQUIRED Variables
#   trajectory(trajectory): int
#   time(time): double
#   time_uv(time): double
#   segment_id(time): int
#   profile_id(time): int
#   depth(time): double
#   depth_qc(time): byte
#   lat(time): double
#   lat_qc(time): byte
#   lon(time): double
#   lon_qc(time): byte
#   pressure(time): double
#   pressure_qc(time): byte
#   conductivity(time): double
#   conductivity_qc(time): byte
#   salinity(time): double
#   salinity_qc(time): byte
#   density(time): double
#   density(time): byte
#   temperature(time): double
#   temperature_qc(time): byte
#   u(time_uv): double
#   u_qc(time_uv): byte
#   v(time_uv): double
#   v_qc(time_uv): byte
#   platform(nodim)
#   instrument_ctd(nodim)
#
# This template is used to generate an empty (no data values) .nc file.  The
# .nc file may then be dumped to .cdl and .ncml.

from datetime import datetime, timedelta
from netCDF4 import default_fillvals as NC_FILL_VALUES;
from netCDF4 import num2date, date2num
from netCDF4 import Dataset
import time as t

# NetCDF4 compression level (1 seems to be optimal, in terms of effort and
# result)
COMP_LEVEL = 1;

# Name of output file (leave v.0.0 pending release of accepted spec):
# kerfoot@marine.rutgers.edu
nc = Dataset('./glider_trajectory_uv_template_v.0.0.nc', 'w', format='NETCDF4_CLASSIC')

# Dimensions
time= nc.createDimension('time', None)
trajectory= nc.createDimension('trajectory', 1)
time_uv= nc.createDimension('time_uv',1)

# Global Attributes
# 2013-07-19 kerfoot@marine.rutgers.edu: haven't looked these over yet
nc.Conventions = "CF-1.6" 
nc.Metadata_Conventions = "Unidata Dataset Discovery v1.0" # TODO: Propose change to ACDD  
nc.acknowledgment = "This deployment partially supported by ..." # 
nc.cdl_template_version = "IOOS_Glider_NetCDF_Trajectory_Template_v0.0" # changed to file_version (?)
nc.cdm_data_type = "Trajectory" 
nc.comment = "This file was created as an example only.  Data is not to be used for scientific purposes." 
nc.contributor_name = "Scott Glenn, Oscar Schofield, John Kerfoot" 
nc.contributor_role = "Principal Investigator, Principal Investigator, Data Manager" 
nc.creator_email = "kerfoot@marine.rutgers.edu" 
nc.creator_name = "John Kerfoot" 
nc.creator_url = "http://marine.rutgers.edu/cool/auvs" 
nc.date_created = "2013-05-08 14:45 UTC" 
nc.date_issued = "2013-05-08 14:45 UTC" 
nc.date_modified = "2013-05-08 14:45 UTC" 
nc.featureType = "trajectory" 
nc.file_version = "IOOS_Glider_NetCDF_Trajectory_Template_v0.0" # TODO Check comparison spreadsheet
nc.geospatial_lat_max = -15.88833 
nc.geospatial_lat_min = -15.9445416666667 
nc.geospatial_lat_resolution = "point" 
nc.geospatial_lat_units = "degrees_north" 
nc.geospatial_lon_max = 1.49547333333333 
nc.geospatial_lon_min = 1.394655 
nc.geospatial_lon_resolution = "point" 
nc.geospatial_lon_units = "degrees_east" 
nc.geospatial_vertical_max = 987.26 
nc.geospatial_vertical_min = 0. 
nc.geospatial_vertical_positive = "down"  # TODO: Better represented as a variable attribute for depth?
nc.geospatial_vertical_resolution = "point" 
nc.geospatial_vertical_units = "meters" 
nc.history = "Created on " + t.ctime(t.time())
nc.id = "ru29-20130507T211956" 
nc.institution = "Institute of Marine & Coastal Sciences, Rutgers University" 
nc.keywords = "Oceans > Ocean Pressure > Water Pressure, Oceans > Ocean Temperature > Water Temperature, Oceans > Salinity/Density > Conductivity, Oceans > Salinity/Density > Density, Oceans > Salinity/Density > Salinity" ;
nc.keywords_vocabulary = "GCMD Science Keywords" 
nc.license = "This data may be redistributed and used without restriction." 
nc.metadata_link = "" 
nc.naming_authority = "edu.rutgers.marine" 
nc.processing_level = "Dataset taken from glider native file format" 
nc.project = "Deployment not project based" 
nc.publisher_email = "kerfoot@marine.rutgers.edu" 
nc.publisher_name = "John Kerfoot" 
nc.publisher_url = "http://marine.rutgers.edu/cool/auvs" 
nc.sea_name = "" 
nc.standard_name_vocabulary = "CF-1.6" # TODO Check CF. Should be CF23 or something similar
nc.source = 'netCDF4 python module tutorial' # CF Definition: 
nc.summary = "The Rutgers University Coastal Ocean Observation Lab has deployed autonomous underwater gliders around the world since 1990. Gliders are small, free-swimming, unmanned vehicles that use changes in buoyancy to move vertically and horizontally through the water column in a saw-tooth pattern. They are deployed for days to several months and gather detailed information about the physical, chemical and biological processes of the world\'s The Slocum glider was designed and oceans. built by Teledyne Webb Research Corporation, Falmouth, MA, USA." ;
nc.time_coverage_end = "2013-05-08 07:56 UTC" 
nc.time_coverage_resolution = "point" 
nc.time_coverage_start = "2013-05-07 21:19 UTC" 
nc.title = "Slocum Glider Dataset" 


# Variable Definitions
# time: no _Fill_Value since dimension
time = nc.createVariable('time',
  'f8',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'axis' : "T",
    'calendar' : 'gregorian',
    'units' : 'seconds since 1970-01-01 00:00:00 UTC',
    'standard_name' : 'time',
    'long_name' : 'Time',
    'observation_type' : 'measured',
    };
for k in sorted(atts.keys()):
  time.setncattr(k, atts[k]);

# time_uv: 64 bit float - no _Fill_Value since dimension
time_uv = nc.createVariable('time_uv',
  'f8',
  ('time_uv',),
  zlib=True,
  complevel=COMP_LEVEL);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'axis' : "T",
    'calendar' : 'gregorian',
    'units' : 'seconds since 1970-01-01 00:00:00 UTC',
    'standard_name' : 'time',
    'long_name' : 'Approximate time midpoint of each segment',
    'observation_type' : 'estimated',
    };
for k in sorted(atts.keys()):
  time_uv.setncattr(k, atts[k]);
# TODO: Add cell_methods here or in u, v

# trajectory: 2 byte integer - no _Fill_Value since dimension
trajectory = nc.createVariable('trajectory',
  'i2',
  ('trajectory',),
  zlib=True,
  complevel=COMP_LEVEL);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'cf_role' : 'trajectory_id',
    'long_name' : 'Unique identifier for each trajectory feature contained in the file',
    'comment' : 'A trajectory can span multiple data files each containing a single segment.',
    };
for k in sorted(atts.keys()):
  trajectory.setncattr(k, atts[k]);


# TODO: Investigate fill value behavior for this library.  See below for a comment from the netcdf4 docs
# The optional keyword fill_value can be used to override the default netCDF _FillValue (the value that the variable gets filled with before any data is written to it, defaults given in netCDF4.default_fillvals). If fill_value is set to False, then the variable is not pre-filled.

# segment_id: 2 byte integer
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
segment_id = nc.createVariable('segment_id',
  'i2',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i2']);
atts = {'comment' : 'Sequential segment number within a trajectory. The set of data collected between 2 gps fixes obtained when the glider surfaces.',
    'long_name' : 'Segment ID',
    'valid_min' : 1,
    'valid_max' : 999,
    'observation_type' : 'calculated',
    };
for k in sorted(atts.keys()):
  segment_id.setncattr(k, atts[k]);

# kerfoot@marine.rutgers.edu: Removed attributes: ancillary_variables, platform

# profile_id: 2 byte integer
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
profile_id = nc.createVariable('profile_id',
  'i2',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i2']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'comment' : 'Sequential profile number within the current in the segment. A profile is defined a single dive or climb', #  TODO: Revise definition'
    'long_name' : 'Profile ID',
    'valid_min' : 1,
    'valid_max' : 999,
    'observation_type' : 'calculated',
    };
for k in sorted(atts.keys()):
  profile_id.setncattr(k, atts[k]);

# kerfoot@marine.rutgers.edu: Removed attributes: ancillary_variables, platform

# Geophysical Variables (time)
# depth: 64 bit float
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
depth = nc.createVariable('depth',
  'f8',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'axis' : 'Z',
    'units' : 'meters',
    'standard_name' : 'depth',
    'valid_min' : 0,
    'valid_max' : 2000,
    'long_name' : 'Depth',
    'reference_datum' : 'sea-surface', # TODO: Check with Stuebe to see if ther is a crs for this.
    'vertical_positive' : 'down', # TODO: Check CF
    'observation_type' : 'calculated',
    'ancillary_variables' : 'depth_qc',
    'platform' : 'platform',
    'instrument' : 'instrument_ctd',
    };
for k in sorted(atts.keys()):
  depth.setncattr(k, atts[k]);

# kerfoot@marine.rutgers.edu: removed 'instrument_ctd' from # ancillary_variables

# depth_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
depth_qc = nc.createVariable('depth_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'depth Quality Flag',
    'standard_name' : 'depth status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  depth_qc.setncattr(k, atts[k]);
#depth_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 
# TODO: I don't think the ancillary_variable reference is intended to be bi-directional.
# kerfoot@marine.rutgers.edu: removed 'ancillary_variable' attribute

# latitude: 64 bit float
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
lat = nc.createVariable('lat',
  'f8',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'axis' : 'Y',
    'units' : 'degrees_north',
    'standard_name' : 'latitude',
    'long_name' : 'Latitude',
    'flag_meanings' : '',
    'valid_min' : -90.,
    'valid_max' : 90.,
    'observation_type' : 'measured',
    'ancillary_variables' : 'lat_qc',
    'platform' : 'platform',
    'comment' : 'Some values are linearly interpolated between measured coordinates.  See lat_qc', # kerfoot@marine.rutgers.edu: Should we interpolate missing values and add a comment ?  If so, what do do with 'observation_type' ?
    };
for k in sorted(atts.keys()):
  lat.setncattr(k, atts[k]);

# lat_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
lat_qc = nc.createVariable('lat_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'lat Quality Flag',
    'standard_name' : 'lat status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  lat_qc.setncattr(k, atts[k]);

#lat_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# longitude: 64 bit float
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
lon = nc.createVariable('lon',
  'f8',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'axis' : 'X',
    'units' : 'degrees_east',
    'standard_name' : 'longitude',
    'long_name' : 'Longitude',
    'flag_meanings' : '',
    'valid_min' : -180.,
    'valid_max' : 180.,
    'observation_type' : 'measured',
    'ancillary_variables' : 'lon_qc',
    'platform' : 'platform',
    'comment' : 'Some values are linearly interpolated between measured coordinates.  See lon_qc', # kerfoot@marine.rutgers.edu: Should we interpolate missing values and add a comment ? If so, what to do with 'observation_type' ?
    };
for k in sorted(atts.keys()):
  lon.setncattr(k, atts[k]);

# lon_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
lon_qc = nc.createVariable('lon_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'lon Quality Flag',
    'standard_name' : 'lon status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  lon_qc.setncattr(k, atts[k]);

#lon_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# pressure: 64 bit float
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
pressure = nc.createVariable('pressure',
  'f8',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'axis' : 'Z',
    'units' : 'dbar',
    'standard_name' : 'pressure',
    'valid_min' : 0,
    'valid_max' : 2000,
    'long_name' : 'Pressure',
    'reference_datum' : 'sea-surface', # TODO: Check with Stuebe to see if ther is a crs for this.
    'vertical_positive' : 'down', # TODO: Check CF
    'observation_type' : 'calculated',
    'ancillary_variables' : 'pressure_qc',
    'platform' : 'platform',
    'instrument' : 'instrument_ctd',
    };
for k in sorted(atts.keys()):
  pressure.setncattr(k, atts[k]);

# kerfoot@marine.rutgers.edu: removed 'instrument_ctd' from # ancillary_variables

# pressure_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
pressure_qc = nc.createVariable('pressure_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'pressure Quality Flag',
    'standard_name' : 'pressure status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  pressure_qc.setncattr(k, atts[k]);

#pressure_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 
# conductivity: 64 bit float
conductivity = nc.createVariable('conductivity',
    'f8',
    ('time',),
    zlib=True,
    complevel=COMP_LEVEL,
    fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'units' : 'S m-1',
    'standard_name' : 'sea_water_electrical_conductivity',
    'valid_min' : 0.,
    'valid_max' : 10.,
    'long_name' : 'Conductivity',
    'observation_type' : 'measured',
    'ancillary_variables' : 'conductivity_qc',
    'platform' : 'platform',
    'instrument' : 'instrument_ctd',
    'coordinates' : 'lon lat depth time',
    };
for k in sorted(atts.keys()):
  conductivity.setncattr(k, atts[k]);

# conductivity_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
conductivity_qc = nc.createVariable('conductivity_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'conductivity Quality Flag',
    'standard_name' : 'conductivity status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  conductivity_qc.setncattr(k, atts[k]);

#conductivity_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# density: 64 bit float
density = nc.createVariable('density',
    'f8',
    ('time',),
    zlib=True,
    complevel=COMP_LEVEL,
    fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'units' : 'kg m-3',
    'standard_name' : 'sea_water_density',
    'valid_min' : 1015.,
    'valid_max' : 1040.,
    'long_name' : 'Density',
    'observation_type' : 'calculated',
    'ancillary_variables' : 'density_qc',
    'platform' : 'platform',
    'instrument' : 'instrument_ctd',
    'coordinates' : 'lon lat depth time',
    };
for k in sorted(atts.keys()):
  density.setncattr(k, atts[k]);

# density_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
density_qc = nc.createVariable('density_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'density Quality Flag',
    'standard_name' : 'density status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  density_qc.setncattr(k, atts[k]);

#density_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# salinity: 64 bit float
salinity = nc.createVariable('salinity',
    'f8',
    ('time',),
    zlib=True,
    complevel=COMP_LEVEL,
    fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'units' : '1e-3',
    'standard_name' : 'sea_water_salinity',
    'valid_min' : 0.,
    'valid_max' : 40.,
    'long_name' : 'Salinity',
    'observation_type' : 'calculated',
    'ancillary_variables' : 'salinity_qc',
    'platform' : 'platform',
    'instrument' : 'instrument_ctd',
    'coordinates' : 'lon lat depth time',
    };
for k in sorted(atts.keys()):
  salinity.setncattr(k, atts[k]);

# salinity_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
salinity_qc = nc.createVariable('salinity_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'salinity Quality Flag',
    'standard_name' : 'salinity status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  salinity_qc.setncattr(k, atts[k]);

#salinity_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# temperature: 64 bit float
temperature = nc.createVariable('temperature',
    'f8',
    ('time',),
    zlib=True,
    complevel=COMP_LEVEL,
    fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'units' : 'Celsius',
    'standard_name' : 'sea_water_temperature',
    'valid_min' : -5.,
    'valid_max' : 40.,
    'long_name' : 'Temperature',
    'observation_type' : 'measured',
    'ancillary_variables' : 'temperature_qc',
    'platform' : 'platform',
    'instrument' : 'instrument_ctd',
    'coordinates' : 'lon lat depth time',
    };
for k in sorted(atts.keys()):
  temperature.setncattr(k, atts[k]);

# temperature_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
temperature_qc = nc.createVariable('temperature_qc',
  'i1',
  ('time',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'temperature Quality Flag',
    'standard_name' : 'temperature status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  temperature_qc.setncattr(k, atts[k]);

#temperature_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# u: 64 bit float
u = nc.createVariable('u',
    'f8',
    ('time_uv',),
    zlib=True,
    complevel=COMP_LEVEL,
    fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'units' : 'm s-1',
    'standard_name' : 'eastward_sea_water_velocity',
    'valid_min' : -10.,
    'valid_max' : 10.,
    'long_name' : 'Eastward Sea Water Velocity',
    'observation_type' : 'calculated',
    'coordinates' : 'time_uv',
    'platform' : 'platform',
    };
for k in sorted(atts.keys()):
  u.setncattr(k, atts[k]);

# u_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
u_qc = nc.createVariable('u_qc',
  'i1',
  ('time_uv',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'u Quality Flag',
    'standard_name' : 'u status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  u_qc.setncattr(k, atts[k]);

#u_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# v: 64 bit float
v = nc.createVariable('v',
    'f8',
    ('time_uv',),
    zlib=True,
    complevel=COMP_LEVEL,
    fill_value=NC_FILL_VALUES['f8']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'units' : 'm s-1',
    'standard_name' : 'northward_sea_water_velocity',
    'valid_min' : -10.,
    'valid_max' : 10.,
    'long_name' : 'Northward Sea Water Velocity',
    'observation_type' : 'calculated',
    'coordinates' : 'time_uv',
    'platform' : 'platform',
    };
for k in sorted(atts.keys()):
  u.setncattr(k, atts[k]);

# v_qc: 1 byte integer (ie: byte)
# kerfoot@marine.rutgers.edu: explicitly specify fill_value when creating
# variable so that it shows up as a variable attribute.  Use the default
# fill_value based on the data type.
v_qc = nc.createVariable('v_qc',
  'i1',
  ('time_uv',),
  zlib=True,
  complevel=COMP_LEVEL,
  fill_value=NC_FILL_VALUES['i1']);
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'long_name' : 'v Quality Flag',
    'standard_name' : 'v status_flag',
    'flag_meanings' : '',
    'valid_min' : 0.,
    'valid_max' : 128.,
    'flag_values' : '',
    };
for k in sorted(atts.keys()):
  v_qc.setncattr(k, atts[k]);

#v_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 

# Container Variables
# platform: 1 byte integer, not dimensioned
platform = nc.createVariable('platform',
    'i1');
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = {'type' : 'platform',
    'id' : 'ru29',
    'wmo_id' : 'ru29',
    'comment' : 'Slocum Glider ru29',
    'long_name' : 'Slocum Glider ru29',
    'instrument' : 'instrument_ctd',
    };
for k in sorted(atts.keys()):
  platform.setncattr(k, atts[k]);

#platform.instrument = "instrument_ctd" # TODO: Add guidance on the wiki to recommend using a comma separated list of instruments?

# instrument_ctd: 1 byte integer, not dimensioned
instrument_ctd = nc.createVariable('instrument_ctd',
    'i1');
# Dictionary of variable attributes.  Use a dictionary so that we can add the
# attributes in alphabetical order (not necessary, but makes it easier to find
# attributes that are in alphabetical order)
atts = { 'serial_number' : '0098',
    'make_model' : 'Seabird SBE 41CP',
    'comment' : 'Slocum Glider ru29',
    'long_name' : 'Seabird SBD 41CP Conductivity, Temperature, Depth Sensor',
    'platform' : 'platform',
    'calibration_date' : '2000-01-01', # ISO 8601 date
    'factory_calibrated' : '',
    'user_calibrated' : '',
    'calibration_report' : '',
    'accuracy' : '', # Different accuracy values for pressure, cond, temp (?)
    'precision' : '', # Different precision values for pressure, cond, temp (?)
    'valid_range' : '', # Different valid_ranges for pressure, cond, temp (?)
    'ancillary_variables' : 'platform temperature temperature_qc conductivity conductivity_qc salinity salinity_qc pressure pressure_qc depth depth_qc density density_qc',
    };
for k in sorted(atts.keys()):
  instrument_ctd.setncattr(k, atts[k]);

## TODO: NODC recommended variable attributes: make_model, serial_number, calibration_date, factory_calibrated, user_calibrated, calibration_report, accuracy, valid_range, and precision. 
## This means we should consider variable specific instrument variables.  e.g. instrument_temperature, instrument_conductivity
##instrument_ctd.ancillary_variables = "platform temperature temperature_qc salinity salinity_qc pressure pressure_qc depth depth_qc conductivity conductivity_qc" ;
## TODO: Look into the proper usage of ancillary_variables.  I think there is a restriction on the axes for ancillary variables that we are abusing.

