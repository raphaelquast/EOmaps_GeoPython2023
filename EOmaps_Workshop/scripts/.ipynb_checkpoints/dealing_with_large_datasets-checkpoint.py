from eomaps import Maps

m = Maps(figsize=(6, 3))
m.all.add_feature.preset.coastline()

m1 = m.new_layer("raster")
m1.set_shape.raster()
m1.set_data(**data1D2D(2000, 2000))
m1.plot_map()
m1.add_colorbar(extend="neither")

print("\nUsing 'raster' as plot shape")
m.snapshot("raster")

m2 = m.new_layer("shade_raster")
m2.add_feature.preset.coastline()
m2.inherit_data(m1)
m2.set_shape.shade_raster()
m2.plot_map()
m2.add_colorbar(extend="neither")


print("Using 'shade_raster' as plot shape")
m.snapshot("shade_raster")