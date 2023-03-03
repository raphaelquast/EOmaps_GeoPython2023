from eomaps import Maps
import matplotlib.pyplot as plt

use_key = "MAPCOLOR13"

# %% Working with GeoDataFrames

def on_layer_activation(m, gdf, val, color="r"):   
    use_gdf = gdf[gdf[use_key] == val]
    m.add_gdf(use_gdf, fc=color, ec="none")

# create a map
m = Maps(layer="all")
m.add_feature.preset.coastline()

# load a dataframe from NaturalEarth
countries = m.add_feature.cultural.admin_0_countries.get_gdf()
m.add_gdf(countries, fc="none", ec="k")

# select the available (unique) keys
usevals = sorted(countries[use_key].unique())
options = {f"{i}" : (i, plt.cm.colors.rgb2hex(plt.cm.tab20(i))) for i in usevals}

# add the (lazily) initialized layers
for name, (val, c) in options.items():
    mi = m.new_layer(name)
    mi.on_layer_activation(on_layer_activation, gdf=countries, val=val, color=c)

# get a widget to select the layers 
m.util.layer_selector(loc="upper center", 
                      draggable=False,
                      layers=list(options),
                      title=use_key,
                      ncol=5,
                      fontsize=9)

m.subplots_adjust(bottom=0)

# %%  GeoDataFrame picking

cmap = plt.cm.colors.ListedColormap([i[1] for i in options.values()])

m2 = Maps(Maps.CRS.Mollweide())
m2.add_feature.preset.coastline()

m2.add_gdf(countries[countries[use_key] > 0], ec="k", column=use_key,
           cmap="tab20", picker_name="key")

def text(m, ID, val, pos, ind):
    return f"{countries.loc[ID].NAME}\n{use_key} = {val}"

m2.cb.pick__key.attach.annotate(text=text)
m2.cb.pick__key.attach.highlight_geometry(ec="r", lw=2, fc="none")