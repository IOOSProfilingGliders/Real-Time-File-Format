# Script to create example glider trajectory file.

from datetime import datetime, timedelta
from netCDF4 import num2date, date2num
from netCDF4 import Dataset
import time as t

nc = Dataset('../examples/trajectory/glider_trajectory_v.0.1.nc', 'w', format='NETCDF4_CLASSIC')

# Dimensions
time =    nc.createDimension('time', None)
trajectory =    nc.createDimension('trajectory', 1)
time_uv =    nc.createDimension('time_uv',1)

# Global Attributes
nc.Conventions = "CF-1.6" 
nc.Metadata_Conventions = "Unidata Dataset Discovery v1.0" # TODO: Propose change to ACDD  
nc.acknowledgment = "This deployment partially supported by ..." # 
#nc.cdl_template_version = "IOOS_Glider_NetCDF_Trajectory_Template_v0.0" changed to file_version
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


# Variable type Definitions
times = nc.createVariable('time','f8',('time',))
times.axis = "T" 
times.calendar = "gregorian" 
times.units = "seconds since 1970-01-01 00:00:00 UTC" 
times.standard_name = "time" 
times.long_name = "Time" 
times.observation_type = "measured" 

time_uvs = nc.createVariable('time_uv','f8',('time_uv',))
time_uvs.axis = "T" 
time_uvs.calendar = "gregorian" 
time_uvs.units = "seconds since 1970-01-01 00:00:00 UTC" 
time_uvs.standard_name = "time" 
time_uvs.long_name = "Approximate time midpoint of each segment" 
time_uvs.observation_type = "estimated" 
# TODO: Add cell_methods here or in u, v


trajectory_id = nc.createVariable('trajectory','i4',('trajectory',))
trajectory_id.cf_role = "trajectory_id" 
trajectory_id.long_name = "Unique identifier for each trajectory feature instance" 
trajectory_id.comment = "A trajectory can span multiple data files each containing a single segment."


# TODO: Investigate fill value behavior for this library.  See below for a comment from the netcdf4 docs
# The optional keyword fill_value can be used to override the default netCDF _FillValue (the value that the variable gets filled with before any data is written to it, defaults given in netCDF4.default_fillvals). If fill_value is set to False, then the variable is not pre-filled.
segment_id = nc.createVariable('segment_id','i4',('time',))
#segment_id._FillValue = -2147483647 # TODO: Check if this is the right syntax
segment_id.comment = "Sequential segment number within a trajectory. The set of data collected between 2 gps fixes obtained when the glider surfaces." ;
segment_id.long_name = "Segment ID" 
segment_id.valid_min = 1 
segment_id.valid_max = 999 
segment_id.observation_type = "calculated"  # TODO: Unnecessary? Potentially confusing. Suggest removing
segment_id.ancillary_variables = "platform profile_id trajectory"  # TODO: Violates definition of ancillary_variable.  Remove.
segment_id.platform = "platform" # TODO: Unnecessary? Potentially confusing. Suggest removing Suggest removing NODC recommends using only with geophysical variables.

profile_id = nc.createVariable('profile_id','i4',('time',))
#profile_id._FillValue = -2147483647 ;
# TODO: Revise definition.  Is this true?  Is it consistent across glider types?
profile_id.comment = "Sequential profile number within the current in the segment. A profile is defined a single dive or climb TODO: Revise definition." ;
profile_id.long_name = "Profile ID" ;
profile_id.valid_min = 1 ;
profile_id.valid_max = 999 ;
profile_id.observation_type = "calculated" ;  # TODO: Unnecessary? Potentially confusing. Suggest removing
profile_id.ancillary_variables = "platform segment_id trajectory" ; # TODO: Violates definition of ancillary_variable.  Remove.
profile_id.platform = "platform" ;  # TODO: Unnecessary? Potentially confusing. Suggest removing NODC recommends using only with geophysical variables.

# Container Variables
platform = nc.createVariable('platform','i4')
platform.type = "slocum" # Controlled vocabulary  {slocum, spray, seaglider}
platform.id = "ru29" ;
platform.wmo_id = "ru29" ;
platform.comment = "Slocum Glider ru29" ;
platform.long_name = "Slocum Glider ru29" ;
platform.instrument = "instrument_ctd" # TODO: Add guidance on the wiki to recommend using a comma separated list of instruments?

instrument_ctd = nc.createVariable('instrument_ctd','i4')
instrument_ctd.comment = "Unpumped CTD with a nominal sampling rate of 1Hz." ;
instrument_ctd.serial_number = -1 ;
instrument_ctd.long_name = "Seabird SBE 41CP Conductivity, Temperature, Depth Sensor." ;
instrument_ctd.make_model = "Seabird  SBE 41CP";
instrument_ctd.platform = "platform" ;
# TODO: NODC recommended variable attributes: make_model, serial_number, calibration_date, factory_calibrated, user_calibrated, calibration_report, accuracy, valid_range, and precision. 
# This means we should consider variable specific instrument variables.  e.g. instrument_temperature, instrument_conductivity
#instrument_ctd.ancillary_variables = "platform temperature temperature_qc salinity salinity_qc pressure pressure_qc depth depth_qc conductivity conductivity_qc" ;
# TODO: Look into the proper usage of ancillary_variables.  I think there is a restriction on the axes for ancillary variables that we are abusing.

# Geophysical Variables (time)
depth = nc.createVariable('depth','f8',('time',),fill_value=9.96920996838687e+36)
#depth._FillValue = 9.96920996838687e+36 
depth.axis = "Z" 
depth.units = "meters" 
depth.standard_name = "depth" 
depth.valid_min = 0. 
depth.valid_max = 2000. 
depth.long_name = "Depth" 
depth.reference_datum = "sea-surface" # TODO: Check with Stuebe to see if ther is a crs for this.
depth.vertical_positive = "down" # TODO: Check CF
depth.observation_type = "calculated" 
depth.ancillary_variables = "depth_qc instrument_ctd" # TODO: only refer to variables with the same shape. Remove instrument_ctd
depth.platform = "platform" 
depth.instrument = "instrument_ctd" 


depth_qc = nc.createVariable('depth_qc','S1',('time',),fill_value=-127b)
depth_qc.long_name = "depth Quality Flag" 
depth_qc.standard_name = "depth status_flag" 
depth_qc.flag_meanings = "" # TODO: Choose QC Flag set for use in the representative case and inthe manual/wiki.  IODE flags? 
depth_qc.valid_range = 0., 128. 
depth_qc.flag_values = "" 
depth_qc.ancillary_variables = "depth instrument_ctd" # TODO: only refer to variables with the same shape. Remove instrument_ctd
# TODO: I don't think the ancillary_variable reference is intended to be bi-directional.

lat = nc.createVariable('lat','f8', ('time',),fill_value=9.96920996838687e+36)
lat.axis = "Y" 
lat.units = "degrees_north" 
lat.standard_name = "latitude" 
lat.valid_min = -90. 
lat.valid_max = 90. 
lat.long_name = "Latitude" 
lat.observation_type = "measured" 
lat.ancillary_variables = "lat_qc" 
lat.platform = "platform" 

nc.createVariable('lat_qc','S1',('time',),fill_value=-127b)
lat_qc.long_name = "lat Quality" 
lat_qc.standard_name = "lat status_flag" 
lat_qc.flag_meanings = "" 
lat_qc.valid_range = 0., 128. 
lat_qc.flag_values = "" 
lat_qc.ancillary_variables = "lat" 

lon = nc.createVariable('lon','f8', ('time',),fill_value=9.96920996838687e+36)
lon.axis = "X" 
lon.units = "degrees_east" 
lon.standard_name = "longitude" 
lon.valid_min = -180. 
lon.valid_max = 180. 
lon.long_name = "Longitude" 
lon.observation_type = "measured" 
lon.ancillary_variables = "lon" 
lon.platform = "platform" 

nc.createVariable('lon_qc','S1',('time',),fill_value=-127b) 
lon_qc.long_name = "lon Quality Flag" 
lon_qc.standard_name = "lon status_flag" 
lon_qc.flag_meanings = "" 
lon_qc.valid_range = 0., 128. 
lon_qc.flag_values = "" 
lon_qc.ancillary_variables = "lon" 

pressure = nc.createVariable('pressure','f8', ('time',),fill_value=9.96920996838687e+36)
pressure.axis = "Z" 
pressure.units = "dbar" 
pressure.standard_name = "pressure" 
pressure.valid_min = 0. 
pressure.valid_max = 2000. 
pressure.long_name = "Pressure" 
pressure.reference_datum = "sea-surface" 
pressure.vertical_positive = "down" 
pressure.observation_type = "measured" 
pressure.ancillary_variables = "pressure_qc instrument_ctd" 
pressure.platform = "platform" 
pressure.instrument = "instrument_ctd" 

nc.createVariable('pressure_qc','S1',('time',),fill_value=-127b) 
pressure_qc.long_name = "pressure Quality" 
pressure_qc.standard_name = "pressure status_flag" 
pressure_qc.flag_meanings = "" 
pressure_qc.valid_range = 0., 128. 
pressure_qc.flag_values = "" 
pressure_qc.ancillary_variables = "pressure instrument_ctd" 

pressure = nc.createVariable('conductivity','f8', ('time',),fill_value=9.96920996838687e+36)
conductivity._FillValue = 9.96920996838687e+36 
conductivity.units = "S m-1" 
conductivity.standard_name = "sea_water_electrical_conductivity" 
conductivity.valid_min = 0. 
conductivity.valid_max = 10. 
conductivity.long_name = "Sea Water Conductivity" 
conductivity.observation_type = "measured" 
conductivity.coordinates = "lon lat depth time" 
conductivity.ancillary_variables = "conductivity instrument_ctd" 
conductivity.platform = "platform" 
conductivity.instrument = "instrument_ctd" 

nc.createVariable('lon_qc','S1',('time',),fill_value=-127b) 
byte conductivity_qc(time) 
conductivity_qc._FillValue = -127b 
conductivity_qc.long_name = "conductivity Quality" 
conductivity_qc.standard_name = "conductivity status_flag" 
conductivity_qc.flag_meanings = "" 
conductivity_qc.valid_range = 0., 128. 
conductivity_qc.flag_values = "" 

pressure = nc.createVariable('pressure','f8', ('time',),fill_value=9.96920996838687e+36)
double density(time) 
density._FillValue = 9.96920996838687e+36 
density.units = "kg m-3" 
density.standard_name = "sea_water_density" 
density.valid_min = 1015. 
density.valid_max = 1040. 
density.long_name = "Sea Water Density" 
density.observation_type = "calculated" 
density.coordinates = "lon lat depth time" 
density.ancillary_variables = "density_qc instrument_ctd" 
density.platform = "platform" 
density.instrument = "instrument_ctd" 

nc.createVariable('lon_qc','S1',('time',),fill_value=-127b) 
byte density_qc(time) 
density_qc._FillValue = -127b 
density_qc.long_name = "density Quality" 
density_qc.standard_name = "density status_flag" 
density_qc.flag_meanings = "" 
density_qc.valid_range = 0., 128. 
density_qc.flag_values = "" 
density_qc.ancillary_variables = "density instrument_ctd" 

pressure = nc.createVariable('pressure','f8', ('time',),fill_value=9.96920996838687e+36)
double salinity(time) 
salinity._FillValue = 9.96920996838687e+36 
salinity.units = "1e-3" 
salinity.standard_name = "sea_water_salinity" 
salinity.valid_min = 0. 
salinity.valid_max = 40. 
salinity.long_name = "Sea Water Salinity" 
salinity.observation_type = "calculated" 
salinity.coordinates = "lon lat depth time" 
salinity.ancillary_variables = "salinity_qc instrument_ctd" 
salinity.platform = "platform" 
salinity.instrument = "instrument_ctd" 

nc.createVariable('lon_qc','S1',('time',),fill_value=-127b) 
byte salinity_qc(time) 
salinity_qc._FillValue = -127b 
salinity_qc.long_name = "salinity Quality" 
salinity_qc.standard_name = "salinity status_flag" 
salinity_qc.flag_meanings = "" 
salinity_qc.valid_range = 0., 128. 
salinity_qc.flag_values = "" 
salinity_qc.ancillary_variables = "salinity instrument_ctd" 

pressure = nc.createVariable('pressure','f8', ('time',),fill_value=9.96920996838687e+36)
double temperature(time) 
temperature._FillValue = 9.96920996838687e+36 
temperature.units = "Celsius" 
temperature.standard_name = "sea_water_temperature" 
temperature.valid_min = -5. 
temperature.valid_max = 40. 
temperature.long_name = "Sea Water Temperature" 
temperature.observation_type = "measured" 
temperature.coordinates = "lon lat depth time" 
temperature.ancillary_variables = "temperature_qc instrument_ctd" 
temperature.platform = "platform" 
temperature.instrument = "instrument_ctd" 

nc.createVariable('lon_qc','S1',('time',),fill_value=-127b) 
byte temperature_qc(time) 
temperature_qc._FillValue = -127b 
temperature_qc.long_name = "temperature Quality" 
temperature_qc.standard_name = "temperature status_flag" 
temperature_qc.flag_meanings = "" 
temperature_qc.valid_range = 0., 128. 
temperature_qc.flag_values = "" 
temperature_qc.ancillary_variables = "temperature instrument_ctd" 


# Depth/Time averaged estiamtes per segment
double u(time_uv) 
u._FillValue = 9.96920996838687e+36 
u.units = "m s-1" 
u.standard_name = "eastward_sea_water_velocity" 
u.valid_min = 0. 
u.valid_max = 3. 
u.long_name = "Eastward Sea Water Velocity" 
u.observation_type = "calculated" 
u.coordinates = "trajectory" 
byte u_qc(trajectory) 
u_qc._FillValue = -127b 
u_qc.long_name = "u Quality" 
u_qc.flag_meanings = "" 
u_qc.valid_range = 0., 128. 
u_qc.flag_values = "" 
u_qc.ancillary_variables = "u" 
double v(trajectory) 
v._FillValue = 9.96920996838687e+36 
v.units = "m s-1" 
v.standard_name = "northward_sea_water_velocity" 
v.valid_min = 0. 
v.valid_max = 3. 
v.long_name = "Northward Sea Water Velocity" 
v.observation_type = "calculated" 
v.coordinates = "trajectory" 
byte v_qc(trajectory) 
v_qc._FillValue = -127b 
v_qc.long_name = "v Quality" 
v_qc.flag_meanings = "" 
v_qc.valid_range = 0., 128. 
v_qc.flag_values = "" 
v_qc.ancillary_variables = "v" 

