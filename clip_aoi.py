from PyQt5.QtWidgets import QFileDialog
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProcessingFeedback, QgsProcessingContext, QgsProject
from qgis import processing


def clip_landfire_evt(iface):
    # Prompt user to select AOI shapefile
    aoi_path, _ = QFileDialog.getOpenFileName(
        iface.mainWindow(), 'Select AOI Shapefile', '', 'Shapefiles (*.shp)')
    if not aoi_path:
        iface.messageBar().pushCritical('Error', 'No AOI shapefile selected')
        return

    # Load AOI shapefile
    aoi_layer = QgsVectorLayer(aoi_path, 'AOI', 'ogr')
    if not aoi_layer.isValid():
        iface.messageBar().pushCritical('Error', 'Invalid AOI shapefile')
        return

    # Get Landfire EVT layer
    landfire_rlayer = QgsProject.instance().mapLayersByName('Landfire EVT')
    if not landfire_rlayer:
        iface.messageBar().pushCritical('Error', 'Landfire EVT layer not found')
        return
    landfire_rlayer = landfire_rlayer[0]

    # Clip Landfire EVT layer to AOI
    params = {
        'INPUT': landfire_rlayer,
        'MASK': QgsProcessingFeatureSourceDefinition(aoi_layer.source(), True),
        'OUTPUT': 'memory:'
    }
    result = processing.run(
        'gdal:cliprasterbymasklayer', 
        params, 
        context=QgsProcessingContext(), 
        feedback=QgsProcessingFeedback()
    )

    clipped_layer = result['OUTPUT']

    # Add clipped layer to project
    QgsProject.instance().addMapLayer(clipped_layer)
    iface.messageBar().pushSuccess('Success', 'Landfire EVT layer clipped to AOI')
