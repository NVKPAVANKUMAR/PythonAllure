import csv
import unittest
from datetime import datetime
import HtmlTestRunner
from requests import get
import logging


class ScrapeMyntraPriceData(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.myntra.com/web/offers/10681246'

    def test_scrape(self):
        response = get(self.url)
        json_response = response.json()
        sweatshirt_price = json_response['price']['discounted']
        with open("Myntra.csv", 'a', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([datetime.now(), sweatshirt_price])

    def tearDown(self):
        logging.info("Execution Completed.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
