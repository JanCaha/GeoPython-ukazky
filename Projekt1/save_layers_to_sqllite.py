from pathlib import Path

from osgeo import ogr

path_data_input = Path(__file__).parent / "data"

new_path = path_data_input / "created"

if not new_path.exists():
    new_path.mkdir(parents=True)

path_data_output = new_path / "data_layers_{}_{}_{}.sqlite".format(2020, 10, "08")

if path_data_output.exists():
    path_data_output.unlink()

output_driver: ogr.Driver = ogr.GetDriverByName("SQLite")
output_ds: ogr.DataSource = output_driver.CreateDataSource(str(path_data_output))

for path in path_data_input.iterdir():

    if path.is_file():
        input_ds: ogr.DataSource = ogr.Open(str(path))

        for i in range(input_ds.GetLayerCount()):

            input_layer: ogr.Layer = input_ds.GetLayerByIndex(i)

            output_ds.CopyLayer(input_layer, "{}-{}".format(path.stem, input_layer.GetName()))

        input_ds = None

output_ds = None
