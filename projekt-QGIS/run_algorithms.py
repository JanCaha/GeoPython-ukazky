from pathlib import Path

# qgis knihovny dvě části, jednak QGIS a modul processing
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms
from qgis.core import QgsApplication

# incializace QGIS
app = QgsApplication([], False)
Processing.initialize()
app.processingRegistry().addProvider(QgsNativeAlgorithms())

path_input_data = Path(__file__).parent.parent / "Projekt1" / "data" / "nc.gpkg"
path_output_points = Path(__file__).parent / "outputs" / "points_nc.gpkg"
path_output_raster = Path(__file__).parent / "outputs" / "raster_nc.tiff"

parameters = {'INPUT': str(path_input_data),
              'POINTS_NUMBER': 100,
              'MIN_DISTANCE': 0,
              'MIN_DISTANCE_GLOBAL': 0,
              'MAX_TRIES_PER_POINT': 10,
              'SEED': None,
              'INCLUDE_POLYGON_ATTRIBUTES': False,
              'OUTPUT': str(path_output_points)}

processing.run("native:randompointsinpolygons",
               parameters=parameters)

result = processing.run("gdal:rasterize",
               {'INPUT': str(path_input_data),
                'FIELD': 'CNTY_ID',
                'BURN': 0,
                'UNITS': 1,
                'WIDTH': 1,
                'HEIGHT': 1,
                'EXTENT': '-84.323900000,-75.457000000,33.882000000,36.589600000 [EPSG:4267]',
                'NODATA': 0,
                'OPTIONS': '',
                'DATA_TYPE': 5,
                'INIT': None,
                'INVERT': False,
                'EXTRA': '',
                'OUTPUT': 'TEMPORARY_OUTPUT'})

print(result)
path_result = result["OUTPUT"]
print(path_result)
