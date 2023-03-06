from eomaps import Maps

m = Maps(figsize=(3,1))
m.add_compass(layer="second", pos=(.1,.1), scale=7, style="north arrow")

m1 = m.new_layer("first")
m1.add_feature.preset.coastline()
m1.add_feature.preset.land()

m1_1 = m1.new_layer()   # A Maps-object on the same layer as m1
m1_1.add_marker(xy=(23, 25), radius=60, ec="k", fc="r", permanent=True)

m2 = m.new_layer("second")
m2.add_feature.preset.ocean()
m2.add_marker(xy=(-50, -30), radius=20, ec="k", fc="#58419c", permanent=True)