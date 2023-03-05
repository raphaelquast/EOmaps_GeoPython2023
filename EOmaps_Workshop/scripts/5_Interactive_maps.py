from eomaps import Maps
import numpy as np

lon = np.linspace(-150,150, 100)
lat = np.linspace(-75, 68, 50)
data = np.random.randint(0, 100, (lon.size, lat.size))
#--------------------------------------------

m = Maps(ax=211)
m.add_feature.preset.coastline()
m.set_data(data, lon, lat)
m.plot_map()

m.cb.click.attach.annotate()
m.cb.click.attach.mark(modifier=1, fc="r", radius=4, radius_crs=4326)
m.cb.click.attach.mark(modifier=2, fc="g", radius=8, radius_crs=4326)
m.cb.click.attach.mark(modifier=3, fc="b", radius=16, radius_crs=4326)


ax = m.f.add_subplot(212)

def cb(ID, pos, val, **kwargs):
    print("\nA custom callback!")
    print(ID, pos, val)
    l, = ax.plot(*pos, marker="o")

    #m.cb.pick.add_temporary_artist(l)

m.cb.pick.attach(cb, button=3)
m.cb.pick.attach.mark(button=3, fc="none", ec="r", buffer=4)