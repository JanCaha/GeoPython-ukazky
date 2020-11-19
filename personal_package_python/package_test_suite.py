import unittest


def test_package():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.discover("tests"))

    print("################################")
    print("{} tests has been found.".format(suite.countTestCases()))
    print("################################")

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == '__main__':
    test_package()
