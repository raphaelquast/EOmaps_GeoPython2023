from eomaps import Maps
import numpy as np

# functions to create random datasets
def data1D(s=500):
    lon = np.random.randint(-150, 150, s)
    lat = np.random.randint(-75, 68, s)
    data = np.random.randint(0, 100, s)
    return dict(data=data, x=lon, y=lat)

def data2D(sx=40, sy=30):
    lon, lat = np.linspace(-160, 50, sx), np.linspace(-70, 80, sy)
    lon, lat = np.meshgrid(lon, lat)
    data = lon**2 + lat**2 + np.cos(lon)
    return dict(data=data, x=lon, y=lat)

def data1D2D(sx=20, sy=30):
    lon = np.linspace(-150,150, sx)
    lat = np.linspace(-75, 68, sy)
    data = np.random.randint(0, 10000, (lon.size, lat.size))
    return dict(data=data, x=lon, y=lat)


m = Maps(ax=221, figsize=(8, 6))
m.add_feature.physical.coastline(fc="none", ec="w", lw=0.5)

# -------------------------------- first map 
m1 = m.new_layer()
m1.set_data(**data1D())
m1.set_classify.EqualInterval(k=5)
m1.set_shape.voronoi_diagram()
m1.plot_map(indicate_masked_points=True)
m1.add_colorbar()

# -------------------------------- second map 
m2 = m.new_map(ax=222)
m2.add_feature.physical.coastline(fc="none", ec="k", lw=0.5)
m2.set_data(**data2D())
m2.set_classify.EqualInterval(k=5)
m2.set_shape.ellipses()
m2.plot_map(vmin=100, vmax=35000, cmap="tab20")
cb = m2.add_colorbar()
cb.tick_params(rotation=90)

# -------------------------------- third map 
m3 = m.new_map(ax=223)
m3.add_feature.physical.coastline(fc="none", ec="k", lw=0.5)
m3.add_feature.preset.ocean()

m3.set_data(**data1D2D(100, 100))
m3.set_classify.EqualInterval(k=5)
m3.set_shape.ellipses()
m3.plot_map(set_extent=False, cmap="cividis")
m3.add_colorbar()

# -------------------------------- inset map for third map 
m3i = m3.new_inset_map(xy=(5,45), radius=15e5, shape="geod_circles",
                       inset_crs=3035,
                       plot_position=(.75, .21), plot_size=.38,
                       indicate_extent=dict(lw=2))
m3i.add_feature.preset.land()
m3i.add_feature.preset.ocean()
m3i.add_gridlines(lw=0.25, zorder=0)


m3i.inherit_data(m3)
m3i.inherit_classification(m3)
m3i.set_shape.ellipses(radius=0.5, radius_crs=4326)
m3i.plot_map()
m3i.text(.5,1.05, "Inset Map", transform=m3i.ax.transAxes, fontsize=12)

m.subplots_adjust(left=0.01, right=.99, bottom=0.01, top=.99, hspace=.25)