from typing import Union
from pathlib import Path

from osgeo import ogr


def open_vector_file(path: Union[Path, str],
                     writeable: bool = True) -> ogr.DataSource:

    if isinstance(path, Path):
        path = str(path.absolute())

    return ogr.Open(path, writeable)
