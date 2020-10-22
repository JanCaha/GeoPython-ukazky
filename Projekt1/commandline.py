from pathlib import Path

import subprocess

path_data = Path(__file__).parent / "data"

problematic_files = []

force_2d = False

for file in path_data.iterdir():

    if file.is_file() and file.suffix == ".gpkg":

        # výsledný formát
        path_output = file.parent / "{}.GML".format(file.stem)

        # konverze do EPSG:4326
        cmd = ["ogr2ogr",
               "-t_srs", "EPSG:4326",
               str(path_output.absolute()), str(file.absolute()),
               "nc"]

        # podle proměnné volat s parametrem
        if force_2d:
            cmd += ["-dim", "XY"]

        run_result: subprocess.CompletedProcess = subprocess.run(cmd)

        if run_result.check_returncode() is not None:
            problematic_files.append(str(file.absolute()))

        print(run_result.args)
        print(run_result.stdout)
        print(run_result.stderr)
        print(run_result.check_returncode())

print(problematic_files)
