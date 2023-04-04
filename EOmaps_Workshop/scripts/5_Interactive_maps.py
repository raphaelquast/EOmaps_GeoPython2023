# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

Turn your maps into interactive data analysis widgets

- Click / Pick / Keypress callbacks
- Pre-defined callbacks
- Custom callbacks

"""

from eomaps import Maps
import numpy as np

lon = np.linspace(-150,150, 100)
lat = np.linspace(-75, 68, 50)
data = np.random.randint(10, 100, (lon.size, lat.size))

def read_data(ID):
    n = np.random.randint(0, 100)
    return np.linspace(-100, 100, n), np.random.randint(-50, 50, n)

m = Maps(ax=211)
m.add_feature.preset.coastline()
m.set_data(data, lon, lat)
m.plot_map()

ax = m.f.add_subplot(212)

# %%

m.cb.click.attach.annotate()

m.cb.click.attach.mark(modifier=1, fc="r", radius=4, radius_crs=4326)
m.cb.click.attach.mark(modifier=2, fc="g", radius=8, radius_crs=4326)
m.cb.click.attach.mark(modifier=3, fc="b", radius=16, radius_crs=4326)

m.cb.pick.attach.annotate(button=3,
                          text = lambda val, **kwargs: f"the value is {val:.2f}"
                          )

m.cb.pick.attach.mark(button=3, fc="none", ec="r", buffer=1)


# %% custom callbacks

def click_cb(ID, pos, val, color="r", markersize=5, **kwargs):
    print("\n", "Clicked at:", pos)
    l, = ax.plot(*pos, marker="o", c=color, markersize=markersize)
    # m.cb.click.add_temporary_artist(l)

def pick_cb(ID, pos, val, **kwargs):
    x, y = read_data(ID)
    l, = ax.plot(x, y)
    # m.cb.pick.add_temporary_artist(l)


m.cb.click.attach(click_cb, button=1, color="b", markersize=2)

m.cb.pick.attach(pick_cb, button=3)