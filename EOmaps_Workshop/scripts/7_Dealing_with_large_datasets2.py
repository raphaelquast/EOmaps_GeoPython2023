# -*- coding: utf-8 -*-
"""   EOmaps GeoPython 2023          ( https://github.com/raphaelquast/EOmaps )

Dealing with large datasets

- Plotting a GeoTIFF (with automatic parsing of the colormap)
- Set the extent prior to plotting to plot only data in the visible extent

"""

# %% Download the data

# =========================================================================
from pathlib import Path
import requests

tilename = "ESA_WorldCover_10m_2020_v100_N45E006_Map.tif"

savepath = Path("datasets") / tilename
if savepath.exists():
    print("file already downloaded")
else:
    print("downloading tile...")

    s3_url_prefix = "https://esa-worldcover.s3.eu-central-1.amazonaws.com"
    url = rf"{s3_url_prefix}/v100/2020/map/{tilename}"
    r = requests.get(url, allow_redirects=True)

    with open(savepath, 'wb') as f:
        f.write(r.content)

# =========================================================================

# %% Create a map
from pathlib import Path
from eomaps import Maps

path = "datasets/ESA_WorldCover_10m_2020_v100_N45E006_Map.tif"

m = Maps.from_file.GeoTIFF(
    path,
    layer="raster",
    extent = "Muttenz",
    shape="raster",
    alpha=0.8,
    )
m.add_gridlines()

for i, r in enumerate([10, 50, 100, 200, 500, 1000, 2000]):
    m.add_marker(xy=(7.6416665, 47.5350134), xy_crs=4326,
                 radius=r, shape="geod_circles",
                 fc="none", ec="k", lw=(i+1)/3)

m.add_annotation(xy=(7.6416665, 47.5350134), xy_crs=4326, text="GeoPython\n2023",
                 xytext=(120,40),
                 horizontalalignment="center",
                 arrowprops=dict(arrowstyle="fancy", fc="k", ec=".5", mutation_scale=30),
                 bbox=dict(boxstyle='circle,pad=0.5', fc='.5')
                )
m.add_logo()

# %% fetch a custom WebMap service and add some layers to the map
url = r"https://ch-osm-services.geodatasolutions.ch/geoserver/ows?service=wms&version=1.3.0&request=GetCapabilities&srsName=EPSG:2056"
wms = m.add_wms.get_service(url)

wms.add_layer.magosm_tram_ltr_routes_line(layer="tram", transparent=True)
wms.add_layer.magosm_railways_line(layer="rail", transparent=True)
wms.add_layer.magosm_hiking_foot_routes_line(layer="hike", transparent=True)

m.show_layer(m.layer, "tram", "rail", "hike")