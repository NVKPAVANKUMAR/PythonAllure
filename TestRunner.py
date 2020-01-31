import unittest

# import your test modules
import HtmlTestRunner

import test_MyntraPriceScrape
import test_ScrapeData_Login
import test_TimeScrape

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_ScrapeData_Login))
suite.addTests(loader.loadTestsFromModule(test_MyntraPriceScrape))
suite.addTests(loader.loadTestsFromModule(test_TimeScrape))

# initialize a runner, pass it your suite and run it
runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', verbosity=2)
runner.run(suite)
