import json
import unittest
from pathlib import Path

import requests


class TestRunner(unittest.TestCase):
    def test_load_json(self):
        with open("C:/Users/npavankumar/PycharmProjects/WebScraping/test.json", "r") as read_file:
            data = json.load(read_file)
        print(data)

    def test_response(self):
        todo_by_user = []
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        response_data = json.loads(response.text)
        for i in response_data:
            if i["completed"]:
                todo_by_user.append(i)
        assert todo_by_user.__sizeof__() is not None

    def test_reqres(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        response_data = json.loads(response.text)
        assert response_data["data"][0]["id"] == 4

    def test_dump_json(self):
        data = {
            "page": 2,
            "per_page": 3,
            "total": 12,
            "total_pages": 4,
            "data": [
                {
                    "id": 4,
                    "email": "eve.holt@reqres.in",
                    "first_name": "Eve",
                    "last_name": "Holt",
                    "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg"
                },
                {
                    "id": 5,
                    "email": "charles.morris@reqres.in",
                    "first_name": "Charles",
                    "last_name": "Morris",
                    "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/stephenmoon/128.jpg"
                },
                {
                    "id": 6,
                    "email": "tracey.ramos@reqres.in",
                    "first_name": "Tracey",
                    "last_name": "Ramos",
                    "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg"
                }
            ]
        }

        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        assert Path('data.json')
