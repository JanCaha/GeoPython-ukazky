from pathlib import Path

from osgeo import gdal

path_raster = Path(__file__).parent / "data" / "elevation.tif"

raster_ds: gdal.Dataset = gdal.Open(str(path_raster))

print(raster_ds.GetDriver())
print(raster_ds.GetLayerCount())
print(raster_ds.RasterCount)
print(raster_ds.RasterXSize)
print(raster_ds.RasterYSize)
print(raster_ds.GetMetadata())

# pásma jsou číslovaná od 1
band_one: gdal.Band = raster_ds.GetRasterBand(1)

print(gdal.GetDataTypeName(band_one.DataType))
print(band_one.GetDescription())

stats = band_one.GetStatistics(True, True)

print(stats)
