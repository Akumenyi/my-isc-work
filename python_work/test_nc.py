from netCDF4 import Dataset

ds = Dataset('/home/user01/ncas-isc/python/exercises/example_data/ggas2014121200_00-18.nc')
for v in ds.variables:
    print v,

sst = ds.variables['SSTK']
print sst

for d in sst.dimensions:
    print d, len(ds.variables[d])

print sst.shape, sst.size

for attr in sst.ncattrs():
    print attr, '=', getattr(sst,attr)

arr = sst[1, 0, 10:20, 30:35]
print type(arr)
dims = sst.dimensions
print dims

vars = ds.variables
arr_tim = vars['time'][1]
arr_lev = vars['surface'][0]
arr_lats = vars['latitude'][10:20]
arr_lons = vars['longitude'][30:35]

for vals in (arr_tim,arr_lev,arr_lats,arr_lons):
    print vals

metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst,attr)
   
print metadata
