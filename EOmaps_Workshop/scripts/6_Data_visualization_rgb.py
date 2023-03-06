# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

Data visualization continued... RGB composites

- A quick showcase how to create RGB (or RGBA) composites

"""

from eomaps import Maps

path = r"datasets/BlueMarbleNG-TB_2004-12-01_rgb_360x180.TIFF"
path_fine = r"datasets/BlueMarbleNG-TB_2004-12-01_rgb_3600x1800.TIFF"



band_data = [Maps.read_file.GeoTIFF(path, sel=dict(band=b)) for b in (1, 2, 3)]
rgb = [d["data"] / 255 for d in band_data]

m = Maps(3035)
#m.set_extent_to_location("europe")
m.set_data(**band_data[0])
m.set_shape.raster()
m.plot_map(fc=rgb)
m.add_gridlines(c="k")



band_data_fine = [
    Maps.read_file.GeoTIFF(path_fine, sel=dict(band=b)) for b in (1, 2, 3)]
rgb_coarse = [d["data"] / 255 for d in band_data_fine]

m2 = m.new_layer("fine")
m2.set_data(**band_data_fine[0])
m2.set_shape.raster()
m2.plot_map(fc=rgb_coarse)
m2.add_gridlines(c="k")

