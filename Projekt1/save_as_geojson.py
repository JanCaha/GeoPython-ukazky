from pathlib import Path

from osgeo import ogr

path_data_input = Path(__file__).parent / "data"

new_path = path_data_input / "created"

if not new_path.exists():
    new_path.mkdir(parents=True)

for path in path_data_input.iterdir():

    if path.is_file():

        path_data_output = new_path / "{}.kml".format(path.stem)

        if path_data_output.exists():
            path_data_output.unlink()

        input_ds: ogr.DataSource = ogr.Open(str(path))

        output_driver: ogr.Driver = ogr.GetDriverByName("KML")
        output_ds: ogr.DataSource = output_driver.CreateDataSource(str(path_data_output))

        input_layer: ogr.Layer = input_ds.GetLayer()

        output_ds.CopyLayer(input_layer, "new_layer")

        output_ds = None
        input_ds = None
