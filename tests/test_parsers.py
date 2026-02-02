import unittest
from pyproject_template.parsers import unstructuredcsv_to_frozenset
import csv

class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Nothing to set up"""

    @classmethod
    def tearDownClass(cls):
        """Nothing to tear down"""

    def test_unstructuredcsv_to_frozenset(self):
        """See function unstructuredcsv_to_frozenset
        for description and implementation details.
        """
        csv_path='tests/data/patternfile.csv'
        csv_values=['WARNING', 'ERROR', 'FAULT']
        fset=unstructuredcsv_to_frozenset(csv_path)
        
        # This assertion is True only if there are no
        # duplication values in the test data.
        self.assertTrue(len(csv_values)==len(fset))

        for value in csv_values:
            self.assertTrue(value in fset)
