from eomaps import Maps

path = r"datasets/BlueMarbleNG-TB_2004-12-01_rgb_3600x1800.TIFF"

band_data = [Maps.read_file.GeoTIFF(p, sel=dict(band=b)) for b in (1, 2, 3)]
rgb = [d["data"] / 255 for d in band_data]

m = Maps(3035)
m.set_extent_to_location("europe")
m.set_data(**band_data[0])
m.set_shape.raster()
m.plot_map(fc=rgb)
m.add_gridlines(c="k")