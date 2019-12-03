import unittest
from app import create_app


class MyTestCase(unittest.TestCase):
    # More test: https://medium.com/grammofy/testing-your-python-api-app-with-json-schema-52677fe73351
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_main_is_json(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.is_json, False)
        self.assertIn("The API is running..", str(res.data))

    def test_endpoint_hello(self):
        res = self.client.get("/hello/", content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.is_json, True)

        json_data = res.json
        assert 'message' in json_data


if __name__ == '__main__':
    unittest.main()
