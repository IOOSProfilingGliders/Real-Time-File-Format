# 

>>> from datetime import datetime, timedelta
>>> from netCDF4 import num2date, date2num
>>> from netCDF4 import Dataset
>>> rootgrp = Dataset('test.nc', 'w', format='NETCDF4_CLASSIC')

>>> level = rootgrp.createDimension('level', None)
>>> time = rootgrp.createDimension('time', None)
>>> lat = rootgrp.createDimension('lat', 73)
>>> lon = rootgrp.createDimension('lon', 144)
>>> times = rootgrp.createVariable('time','f8',('time',))
>>> levels = rootgrp.createVariable('level','i4',('level',))
>>> latitudes = rootgrp.createVariable('latitude','f4',('lat',))
>>> longitudes = rootgrp.createVariable('longitude','f4',('lon',))
>>> # two dimensions unlimited.
>>> temp = rootgrp.createVariable('temp','f4',('time','level','lat','lon',))
setncattr(self, name, value)
>>> import time
>>> rootgrp.description = 'bogus example script'
>>> rootgrp.history = 'Created ' + time.ctime(time.time())
>>> rootgrp.source = 'netCDF4 python module tutorial'
>>> latitudes.units = 'degrees north'
>>> longitudes.units = 'degrees east'
>>> levels.units = 'hPa'
>>> temp.units = 'K'
>>> times.units = 'hours since 0001-01-01 00:00:00.0'
>>> times.calendar = 'gregorian'