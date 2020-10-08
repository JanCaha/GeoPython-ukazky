from pathlib import Path

from osgeo import ogr

path_data_input = Path(__file__).parent / "data" / "nc.gpkg"

input_ds: ogr.DataSource = ogr.Open(str(path_data_input), True)

input_layer: ogr.Layer = input_ds.GetLayerByName("nc")

input_ds.CreateLayer("centroids",
                     srs=input_layer.GetSpatialRef(),
                     geom_type=ogr.wkbPoint,
                     options=["OVERWRITE=YES"])

output_layer: ogr.Layer = input_ds.GetLayerByName("centroids")

idField: ogr.FieldDefn = ogr.FieldDefn("id", ogr.OFTInteger)
output_layer.CreateField(idField)

feature: ogr.Feature

i = 1
for feature in input_layer:

    geom: ogr.Geometry = feature.GetGeometryRef()

    point_geom: ogr.Geometry = geom.Centroid()

    # print(point_geom.ExportToWkt())

    featureDefn: ogr.FeatureDefn = output_layer.GetLayerDefn()
    new_feature: ogr.Feature = ogr.Feature(featureDefn)
    new_feature.SetGeometry(point_geom)
    new_feature.SetField("id", i)
    output_layer.CreateFeature(new_feature)

    print(i)
    i += 1

input_ds = None