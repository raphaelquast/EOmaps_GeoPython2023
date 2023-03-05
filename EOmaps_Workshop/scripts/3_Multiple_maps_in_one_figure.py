# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

Dealing with multiple maps and/or plots in a single figure.

- Adding new maps/axes to the figure
- InsetMaps
- Re-positioning of axes
- Using the Layout Editor                     >>> Keyboard Shortcut:  "alt + l"

"""

from eomaps import Maps

m = Maps(ax=321)
m.add_feature.preset.coastline()

m1 = m.new_map(ax=322)
m1.add_feature.preset.countries(zorder=0)

m2 = m.new_map(ax=323, crs=Maps.CRS.Mollweide())
m2.add_feature.physical.land(fc="#97c1aa")

m3 = m.new_map(ax=324, crs=Maps.CRS.InterruptedGoodeHomolosine())
m3.add_feature.preset.ocean()

m5 = m.new_map(ax=325, crs=Maps.CRS.Orthographic(-60, -20), keep_on_top=True)
m5.add_feature.preset.ocean()
m5.add_feature.physical.land(fc="darkgreen", ec="none")


# --- create an InsetMap
m2i = m2.new_inset_map(xy=(-60, -15), radius=(35, 50),
                       inset_crs=Maps.CRS.Stereographic(), shape="rectangles",
                       plot_position=(.85, .8), plot_size=0.35,
                       indicate_extent=False)
m2i.add_feature.physical.ocean(fc="lightblue")
m2i.add_feature.physical.land(fc="g", ec="k")
gl = m2i.add_gridlines(lw=0.25)

for i in (m, m1, m2, m3, m5):
    m2i.indicate_inset_extent(i, fc=(1, 0, 0, 0.25))


# --- create an ordinary axes
ax = m.f.add_subplot(326, zorder=100)
ax.scatter(range(10), range(10), c=range(10))