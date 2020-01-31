import unittest
from datetime import datetime

import pytest
from requests import post


class ScrapeTSRTCData(unittest.TestCase):
    def getDate(cls):
        cls.now = datetime.now()
        return cls.now.strftime("%Y-%M-%d")

    def setUp(self):
        self.mydict = {'arg3': self.getDate(),
                       'arg1': '7902',
                       'arg2': '3'
                       }
        self.url_endpoint = 'https://www.abhibus.com/getonewayservices/2020-01-30/7902/3'

    @pytest.mark.skip
    def test_TSRTC(self):
        response = post(self.url_endpoint)
        print(response.url)
        pass
        # json_response = response.json()
        # bus_count = json_response['serviceDetailsList']
        # print(bus_count)
