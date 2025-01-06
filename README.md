# Basemap Landfire EVT Plugin
Loads the Landfire EVT and a OpenStreetMap basemap. Also want to add the following functions:

1. Loads a shp file as an AOI
2. Clips the AOI to Landfire EVT
3. Generates a conservation target map with % of each EVT class to the AOI
4. Add global human mod database and imperiled spp. richness, e.g., t&e species tif from Wildfire Task Force RRKs



## How to use the plugin with QGIS

1. Create a new python plugin directory
  * e.g. Linux ```~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/minimal```
  * e.g. Windows ```C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\minimal```
  * e.g. macOS ```~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/minimal```
2. Copy ```metadata.txt``` and ```__init__.py``` to that directory
3. Start QGIS and enable the plugin (menu Plugins > Manager and Install Plugins...)

Now you should see a "Go!" button in your "Plugins" toolbar (make sure it is enabled in menu Settings > Toolbars > Plugins).

The next step is to change the metadata (e.g. plugin title and description) in ```metadata.txt``` and
start adding your own code to ```__init__.py```. Have fun!

Based on the QGIS minimalist plugin skeleton.
