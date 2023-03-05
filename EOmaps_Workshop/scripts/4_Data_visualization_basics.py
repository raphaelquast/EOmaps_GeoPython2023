from eomaps import Maps
import numpy as np


# functions to create random datasets
def data1D(s=500):
    lon = np.random.randint(-150, 150, s)
    lat = np.random.randint(-75, 68, s)
    data = np.random.randint(0, 100, s)
    return data, lon, lat


def data2D(sx=40, sy=30):
    lon, lat = np.linspace(-160, 50, sx), np.linspace(-70, 80, sy)
    lon, lat = np.meshgrid(lon, lat)
    data = lon**2 + lat**2 + np.cos(lon)
    return data.astype(int), lon, lat


def data1D2D(sx=20, sy=30):
    lon = np.linspace(-150, 150, sx)
    lat = np.linspace(-75, 68, sy)
    data = np.random.randint(0, 10000, (lon.size, lat.size))
    return data, lon, lat


#data, lon, lat = data1D(500)
#data, lon, lat = data1D2D(50, 50)
data, lon, lat = data1D2D(50,50)

m = Maps(figsize=(8, 6))
m.add_feature.preset.coastline()

m1 = m.new_layer()
m1.set_data(data=data, x=lon, y=lat, crs=4326,
            encoding=dict(scale_factor=1/10000, add_offset=0)
            )

# m1.set_classify.EqualInterval(k=5)
# m1.set_classify.Quantiles(k=5)
#m1.set_classify.UserDefined(bins=[10,20,30,500])

# m1.set_shape.ellipses()
# m1.set_shape.rectangles()
# m1.set_shape.geod_circles(radius=2e5)
# m1.set_shape.voronoi_diagram()
# m1.set_shape.delaunay_triangulation()
# m1.set_shape.scatter_points()
# m1.set_shape.raster()

m1.plot_map()                           # plot the map

m1.add_colorbar()                       # add a colorbar



# %%
m_inset = m.new_inset_map(xy=(5, 45), radius=15e5, shape="geod_circles")
m_inset.add_feature.preset.coastline()
m_inset.add_feature.preset.ocean()
m_inset.add_feature.preset.land()
m_inset.inherit_data(m1)
m_inset.inherit_classification(m1)

#m_inset.set_shape.raster()

m_inset.plot_map()
