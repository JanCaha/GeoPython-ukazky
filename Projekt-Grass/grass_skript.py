from pathlib import Path
import os
import shutil

from grass.script import core as gcore
import grass.script as gscript
import grass.script.setup as gsetup


path_data = Path(__file__).parent / "data"

epsg = "EPSG:5514"

os.environ['GISBASE'] = r'I:\OSGeo4W64\apps\grass\grass78'

path_grass_data = "I:/grass"
location_name = "test_data"

path_grass = Path(path_grass_data) / location_name

if path_grass.exists():
    shutil.rmtree(str(path_grass))

gsetup.init(os.environ['GISBASE'])

gcore.create_location(path_grass_data, location_name)
gsetup.init(os.environ['GISBASE'], path_grass_data, location_name)

result_rasters = []


for path_file in path_data.iterdir():

    file = str(path_file.absolute())

    imported = path_file.stem.split("_")[0]

    region = gscript.parse_command("r.in.xyz",
                                   input=file,
                                   separator="space",
                                   flags="sg",
                                   output="bbox",
                                   parse=(gcore.parse_key_val, {'sep': '=', 'vsep': ' '}))

    gscript.run_command("g.region",
                        res="1",
                        flags="p",
                        **region)

    gscript.run_command("r.in.xyz",
                        input=file,
                        output=imported,
                        method="median",
                        separator="space")

    int_rast_name = imported + "_int1000"

    gscript.run_command("r.mapcalc",
                        expression="{} = int({}@PERMANENT * 1000)".format(int_rast_name,
                                                                          imported))

    # gscript.run_command("g.remove",
    #                     type="raster",
    #                     name=imported + "@PERMANENT")

    interpolated_name = imported + "_i"

    gscript.run_command("r.surf.idw",
                        input=int_rast_name,
                        output=interpolated_name)

    gscript.run_command("g.remove",
                        type="raster",
                        name=int_rast_name + "@PERMANENT",
                        flag="f")

    double_rast_name = imported + "_i_double"

    gscript.run_command("r.mapcalc",
                        expression="{} = double({}@PERMANENT) / 1000".format(double_rast_name,
                                                                             interpolated_name))

    # gscript.run_command("g.remove",
    #                     type="raster",
    #                     name=interpolated_name + "@PERMANENT")

    result_rasters.append("{}@PERMANENT".format(double_rast_name))

    print("File {} done!".format(path_file))

input_rasters = ",".join(result_rasters)

region = gscript.parse_command("g.region",
                               raster=input_rasters,
                               flags="sg")

params = {key: value for key, value in region.items() if key in ["n", "s", "e", "w"]}

gscript.run_command("g.region",
                    res="1",
                    flags="p",
                    **params)

output_name = "Result_DSM"

gscript.run_command("r.patch",
                    input=input_rasters,
                    output=output_name)

gscript.run_command("r.out.gdal",
                    input="{}@PERMANENT".format(output_name),
                    output="D:/{}.tiff".format(output_name),
                    format="GTiff")
