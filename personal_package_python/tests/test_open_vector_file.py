from pathlib import Path
import os
import unittest

from osgeo import ogr

from personalpackage.ogr import open_vector_file


class CmdTests(unittest.TestCase):

    def test_open_vector_file(self):

        path = os.path.join(os.path.dirname(__file__), "test_data", "nc.gpkg")

        self.assertIsInstance(open_vector_file(path), ogr.DataSource)

        path = Path(__file__).parent / "test_data" / "nc.gpkg"

        self.assertIsInstance(open_vector_file(path), ogr.DataSource)
