import unittest
from datetime import datetime
import stock_visualizer_2 


class TestStockVisualizerInput(unittest.TestCase):
    def test_stock_symbol_input(self):
        # Valid symbol
        self.assertTrue("stock_symbol", "AAPL")

        # Invalid symbol (length exceeds 7)
        self.assertFalse("stock_symbol", "ABCDEFGHI")

        # Invalid symbol (lowercase)
        self.assertFalse("stock_symbol", "aapl")

    def test_chart_type_input(self):
        # Valid chart type
        self.assertTrue("chart_type", "1")

        # Invalid chart type (not numeric)
        self.assertFalse("chart_type", "ABC")

        # Invalid chart type (numeric but not 1 or 2)
        self.assertFalse("chart_type", "3")

    def test_time_series_input(self):
        # Valid time series
        self.assertTrue("time_series", "3")

        # Invalid time series (not numeric)
        self.assertFalse("time_series", "ABC")

        # Invalid time series (numeric but not 1-4)
        self.assertFalse("time_series", "5")

    def test_start_date_input(self):
        # Valid start date
        self.assertTrue("start_date", "2022-01-01")

        # Invalid start date (wrong format)
        self.assertFalse("start_date", "2022/01/01")

    def test_end_date_input(self):
        # Valid end date
        self.assertTrue("end_date", "2022-12-31")

        # Invalid end date (wrong format)
        self.assertFalse("end_date", "2022/12/31")


if __name__ == "__main__":
    unittest.main()
