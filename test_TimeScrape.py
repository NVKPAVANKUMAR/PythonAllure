import unittest
import HtmlTestRunner
from bs4 import BeautifulSoup
from requests import get


class TestRunner(unittest.TestCase):
    def test_timescrape(self):
        url = 'https://www.timeanddate.com/worldclock/india/new-delhi'
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        time_container = html_soup.find('span', class_='h1')
        print(time_container.get_text())


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
