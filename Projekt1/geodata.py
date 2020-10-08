from osgeo import ogr

data: ogr.DataSource = ogr.Open("./data/nc.gpkg")

print(data)

print("Počet vrstev je {} v datové sadě {}.".format(data.GetLayerCount(),
                                                    data.GetName()))

vrstva: ogr.Layer = data.GetLayer()

print(vrstva)

print("Ve vrstvě {} je {} prvků.".format(vrstva.GetName(),
                                         vrstva.GetFeatureCount()))
prvek: ogr.Feature

for prvek in vrstva:

    print(prvek.GetField(4))
