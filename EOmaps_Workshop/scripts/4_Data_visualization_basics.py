# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

Data Visualization Basics

- 1D / 2D Datasets
- Data Classification
- Plot "Shapes"
- Colorbars
- InsetMaps

"""

from eomaps import Maps
import numpy as np
import pandas as pd

# functions to create random datasets
def get_data_1d(s=500):
    lon = np.random.randint(-150, 150, s)
    lat = np.random.randint(-75, 68, s)
    data = np.random.normal(50, 20, s)
    return data, lon, lat

def get_data_2d(sx=40, sy=30):
    lon, lat = np.linspace(-160, 50, sx), np.linspace(-70, 80, sy)
    lon, lat = np.meshgrid(lon, lat)
    data = np.random.normal(50, 20, lon.shape)
    return data.astype(int), lon, lat

def get_data_1d2d(sx=20, sy=30):
    lon = np.linspace(-150, 150, sx)
    lat = np.linspace(-75, 68, sy)
    data = np.random.normal(50, 20, (lon.size, lat.size))
    return data, lon, lat

def get_data_pandas(s=500):
    data, lon, lat = get_data_1d(s)
    df = pd.DataFrame(dict(data=data, lon=lon, lat=lat))
    return df 

data_1d, lon_1d, lat_1d = get_data_1d(500)
data_2d, lon_2d, lat_2d = get_data_2d(50, 70)
data_1d2d, lon_1d2d, lat_1d2d = get_data_1d2d(50, 70)
df = get_data_pandas(500)


# %%

m = Maps(figsize=(8, 6))
m.add_feature.preset.coastline()

m1 = m.new_layer()

m1.set_data(data=data_1d, x=lon_1d, y=lat_1d, crs=4326)
# m1.set_data(data=data_2d, x=lon_2d, y=lat_2d, crs=4326)
# m1.set_data(data=data_1d2d, x=lon_1d2d, y=lat_1d2d, crs=4326)
# m1.set_data(data=df, x="lon", y="lat", parameter="data", crs=4326)

# m1.set_classify.EqualInterval(k=5)
# m1.set_classify.Quantiles(k=5)
# m1.set_classify.UserDefined(bins=[10,20,30,500])

# m1.set_shape.ellipses()
# m1.set_shape.rectangles()
# m1.set_shape.geod_circles(radius=2e5)
# m1.set_shape.voronoi_diagram()
# m1.set_shape.delaunay_triangulation()
# m1.set_shape.scatter_points()
# m1.set_shape.raster()

m1.plot_map(cmap="viridis", vmin=0, vmax=100, indicate_masked_points=True)

m1.add_colorbar(hist_bins=20)

# %%
m_inset = m.new_inset_map(xy=(5, 45), radius=15e5, shape="geod_circles")
m_inset.add_feature.preset.coastline()
m_inset.add_feature.preset.ocean()
m_inset.add_feature.preset.land()
m_inset.inherit_data(m1)
m_inset.inherit_classification(m1)

#m_inset.set_shape.raster()

m_inset.plot_map()
