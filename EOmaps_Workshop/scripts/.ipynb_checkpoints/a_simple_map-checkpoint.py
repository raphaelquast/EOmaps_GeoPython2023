from eomaps import Maps

m = Maps(Maps.CRS.Mollweide())
m.set_extent((-50, 50, -20, 20))

m.add_feature.preset.coastline()
m.add_feature.preset.ocean()
m.add_feature.physical.land(fc="#c2c9a2")

m.add_gridlines(5, c=".5")
m.add_compass(pos=(.105, .76), scale=12, style="north arrow")
s = m.add_scalebar(
    auto_position=(0.68, 0.25),
    autoscale_fraction=0.45, 
    patch_props=dict(fc="#d8dace", ec="none", alpha=0.75))

m.add_logo()