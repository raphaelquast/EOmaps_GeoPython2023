# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

# Layer-management ... compare and combine plot-layers!

- Create new layers    (layers are "lazy", they are only plotted if visible!)
- Combine and overlay multiple layers
- Layer "peeking"
- A first look at the "companion-widget"            >>> Keyboard Shortcut:  "w"

"""

from eomaps import Maps

m = Maps()
m.add_feature.preset.coastline()

m1 = m.new_layer("land")
m1.add_feature.preset.land()

m1_1 = m1.new_layer()   # A Maps-object on the same layer as m1
m1_1.add_marker(xy=(23, 25), radius=60, ec="k", fc="red", permanent=True)


m2 = m.new_layer("ocean")
m2.add_feature.preset.ocean()
m2.add_marker(xy=(-50, -30), radius=20, ec="k", fc="#58419c", permanent=True)

m.show_layer("land")                           # show an individual layer
m.show_layer("ocean", "land", "base")          # overlay multiple layers
m.show_layer("ocean", ("land", 0.5), "base")   # transparent overlays

# adding WebMap layers
m.add_wms.OpenStreetMap.add_layer.default(layer="OSM_WMS")