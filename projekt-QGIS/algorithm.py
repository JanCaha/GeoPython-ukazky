from pathlib import Path

from PyQt5.QtCore import QVariant

from qgis.core import QgsApplication
from qgis.core import (
    QgsVectorLayer,
    QgsFeatureIterator,
    QgsFeature,
    QgsGeometry,
    QgsFields,
    QgsField,
    QgsVectorFileWriter,
    QgsWkbTypes)

app = QgsApplication([], False)

path_input_layer = Path(__file__).parent.parent / "Projekt1" / "data" / "nc.gpkg"

path_output_layer = Path(__file__).parent / "outputs" / "convex_hull_nc.gpkg"

layer_input: QgsVectorLayer = QgsVectorLayer(str(path_input_layer))

features: QgsFeatureIterator = layer_input.getFeatures()

fields: QgsFields = QgsFields()
fields.append(QgsField("name", QVariant.String))

writer: QgsVectorFileWriter = QgsVectorFileWriter(str(path_output_layer),
                                                  "UTF-8",
                                                  fields,
                                                  QgsWkbTypes.Polygon,
                                                  layer_input.sourceCrs())

feature: QgsFeature

for feature in features:

    attrs = feature.attributes()
    print(attrs)

    geom: QgsGeometry = feature.geometry()
    print(geom.asWkt())

    f = QgsFeature(fields)
    f.setAttribute("name", feature.attribute("NAME"))
    f.setGeometry(geom.convexHull())

    writer.addFeature(f)

del writer
