from pathlib import Path

from qgis.core import QgsApplication
from qgis.core import (
    QgsVectorLayer,
    QgsFeatureIterator,
    QgsFeature,
    QgsGeometry,
    QgsFields,
    QgsVectorFileWriter,
    QgsWkbTypes)

app = QgsApplication([], False)

path_input_layer = Path(__file__).parent.parent / "Projekt1" / "data" / "nc.gpkg"

path_output_layer = path_output_points = Path(__file__).parent / "outputs" / "centroids_nc.gpkg"

layer_input: QgsVectorLayer = QgsVectorLayer(str(path_input_layer))

features: QgsFeatureIterator = layer_input.getFeatures()

feature: QgsFeature

fields: QgsFields = QgsFields()

writer:  QgsVectorFileWriter = QgsVectorFileWriter(str(path_output_layer),
                                                   "UTF-8",
                                                   fields,
                                                   QgsWkbTypes.Point,
                                                   layer_input.sourceCrs())

for feature in features:

    attrs = feature.attributes()
    print(attrs)

    geom: QgsGeometry = feature.geometry()

    print(geom.asWkt())

    f = QgsFeature(fields)
    f.setGeometry(geom.centroid())

    writer.addFeature(f)
