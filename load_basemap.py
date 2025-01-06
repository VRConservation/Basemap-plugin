import os
import inspect
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from qgis.core import QgsRasterLayer, QgsProject, QgsPointXY
from qgis.core import QgsDataSourceUri, QgsProject, QgsVectorLayer
from owslib.wfs import WebFeatureService
# from .clip_aoi import clip_landfire_evt  # Import the clipping function

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]


class BasemapLoaderPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        icon = os.path.join(os.path.join(cmd_folder, 'logo.png'))
        self.action = QAction(QIcon(icon), 'Load Basemap', self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action


    def run(self):
        # Set the map center and zoom level
        canvas = self.iface.mapCanvas()
        center_point = QgsPointXY(-98.5795, 39.8283)
        canvas.setCenter(center_point)
        canvas.zoomScale(5000000)  # Adjust the scale as needed
        canvas.refresh()

        # load open streetmap basemap
        basemap_url = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
        zmin = 0
        zmax = 19
        crs = 'EPSG:3857'

        uri = f'type=xyz&url={basemap_url}&zmax={zmax}&zmin={zmin}$crs={crs}'
        rlayer = QgsRasterLayer(uri, 'OpenStreetMap', 'wms')
        if rlayer.isValid():
            QgsProject.instance().addMapLayer(rlayer)
            self.iface.messageBar().pushSuccess('Success', 'Basemap Layer Loaded')
        else:
            self.iface.messageBar().pushCritical('Error', 'Invalid Basemap Layer')

    # Load Landfire EVT layer
        landfire_url = 'https://lfps.usgs.gov/arcgis/rest/services/Landfire_LF240/US_240EVT/ImageServer'
        landfire_uri = f'url={landfire_url}'
        landfire_rlayer = QgsRasterLayer(
            landfire_uri, 'Landfire EVT', 'arcgismapserver')
        if landfire_rlayer.isValid():
            QgsProject.instance().addMapLayer(landfire_rlayer)
            self.iface.messageBar().pushSuccess('Success', 'Landfire EVT Layer Loaded')
        else:
            self.iface.messageBar().pushCritical('Error', 'Invalid Landfire EVT Layer')

    # # Load Human Modified Lands layer adds layer but layer doesn't work. works in arcgis
    #     human_modified_url = 'https://tiledimageservices.arcgis.com/jIL9msH9OI208GCb/arcgis/rest/services/Human_Modified_Lands/ImageServer'
    #     human_modified_uri = f'url={human_modified_url}'
    #     human_modified_rlayer = QgsRasterLayer(
    #         human_modified_uri, 'Human Modified Lands', 'arcgismapserver')
    #     if human_modified_rlayer.isValid():
    #         QgsProject.instance().addMapLayer(human_modified_rlayer)
    #         self.iface.messageBar().pushSuccess('Success', 'Human Modified Lands Layer Loaded')
    #     else:
    #         self.iface.messageBar().pushCritical('Error', 'Invalid Human Modified Lands Layer')