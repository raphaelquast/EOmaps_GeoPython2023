# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

# The basics of EOmaps

- Map projections
- Features from NaturalEarth (https://www.naturalearthdata.com/)
- Gridlines, North-Arrows, Scalebars, Logos
"""

from eomaps import Maps

m = Maps(crs=4326, figsize=(8, 4))
m.set_extent((-50, 50, -20, 20))

m.add_feature.preset.coastline()
m.add_feature.preset.ocean()

m.add_feature.cultural.admin_0_countries(scale=50, zorder=10,
                                         fc="#c2c9a2", lw=0.5, ec="k")

m.add_gridlines(5, c=".5")

m.add_compass(pos=(.105, .76), scale=12, style="north arrow")

s = m.add_scalebar(
    auto_position=(0.68, 0.25),
    autoscale_fraction=0.45,
    patch_props=dict(fc="#d8dace", ec="none", alpha=0.75))

m.add_logo()
