# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

Dealing with large datasets

- Plotting raster-data
- Using datashader

"""


from eomaps import Maps
import numpy as np

lon = np.linspace(-150,150, 2000)
lat = np.linspace(-75, 68, 2000)
data = np.random.randint(0, 100, (lon.size, lat.size))
#--------------------------------------------

m = Maps(layer="all", figsize=(6, 3))
m.add_feature.preset.coastline()

m1 = m.new_layer("raster")
m1.set_shape.raster()
m1.set_data(data, lon, lat)
m1.plot_map()
m1.add_colorbar(extend="neither", hist_bins=50)

m2 = m.new_layer("shade_raster")
m2.add_feature.preset.coastline()
m2.inherit_data(m1)
m2.set_shape.shade_raster()
m2.plot_map()
m2.add_colorbar(extend="neither", hist_bins=50,
                #dynamic_shade_indicator=True
                )

m.util.layer_selector(layers=[m1.layer, m2.layer], ncol=2, fontsize=7)
m.show_layer("raster")
