from eomaps import Maps

m = Maps(ax=221)
m.add_feature.preset.coastline()

m2 = m.new_map(ax=222)
m2.add_feature.preset.countries(zorder=0)

m3 = m.new_map(ax=223, crs=Maps.CRS.Mollweide())
m3.add_feature.physical.land(fc="#97c1aa")

m4 = m.new_map(ax=224, crs=Maps.CRS.InterruptedGoodeHomolosine())
m4.add_feature.preset.ocean()

m5 = m.new_map(ax=335, crs=Maps.CRS.Orthographic(-60, -20), keep_on_top=True)
m5.add_feature.preset.ocean()
m5.add_feature.physical.land(fc="darkgreen", ec="none")

# --- create an InsetMap
m2i = m2.new_inset_map(xy=(-60,-15), radius=(35, 50), 
                       inset_crs=Maps.CRS.Stereographic(), shape="rectangles", 
                       plot_position=(.85, .8), plot_size=0.35, 
                       indicate_extent=False)
m2i.add_feature.physical.ocean(fc="lightblue")
m2i.add_feature.physical.land(fc="g", ec="k")
m2i.add_gridlines(lw=0.25)
for i in (m, m2, m3, m4, m5):
    m2i.indicate_inset_extent(i, fc=(1,0,0,.25))