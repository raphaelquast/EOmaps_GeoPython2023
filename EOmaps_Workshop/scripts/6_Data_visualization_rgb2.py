from eomaps import Maps
import xarray as xar

path = r"datasets/BlueMarbleNG-TB_2004-12-01_rgb_3600x1800.TIFF"


with xar.open_dataset(path, mask_and_scale=False) as ncfile:
    x, y = ncfile.x.values, ncfile.y.values
    data = ncfile.isel(band=[0,1,2]).band_data.values.transpose(0, 2, 1) / 255
    rgb = [*data]
    
    
m = Maps()
m.set_extent_to_location("europe")
m.set_data(None, x, y)
m.set_shape.raster()
m.plot_map(fc=rgb)
m.add_gridlines(c="k")