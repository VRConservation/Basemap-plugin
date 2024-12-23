# modified from the original qgis minimal plugin at  the repo https://github.com/wonder-sk/qgis-minimal-plugin/tree/master

from .load_basemap import BasemapLoaderPlugin

def classFactory(iface):
    return BasemapLoaderPlugin(iface)
