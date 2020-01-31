import unittest

import HtmlTestRunner
import requests
from bs4 import BeautifulSoup


class ScrapeSiteLoginData(unittest.TestCase):
    def setUp(self):
        self.url = 'https://opensource-demo.orangehrmlive.com/index.php'

    def test_scrape(self):
        session = requests.Session()
        payload = {
            'txtUsername': 'Admin',
            'txtPassword': 'admin123'
        }
        s = session.post(self.url + '/auth/validateCredentials', data=payload)
        s = session.get(self.url + '/dashboard')
        soup = BeautifulSoup(s.text, 'html.parser')
        self.assertIsNotNone(soup.find('img')['src'])


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
