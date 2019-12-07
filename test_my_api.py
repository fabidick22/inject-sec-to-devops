import unittest
from app import create_app
import cProfile
import pstats
import io
import time


BOLD = '\033[1m'
END = '\033[0m'


class MyTestCase(unittest.TestCase):
    # More test: https://medium.com/grammofy/testing-your-python-api-app-with-json-schema-52677fe73351
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.methods = {"get": self.client.get, "post": self.client.get}

    def make_profile_endpoint(self, endpoint: str, method: str):
        header_fill_char = "-"
        body_fill_char = "#"
        title_size = 60
        subtitle_size = 5
        call_endpoint = self.methods.get(method, None)
        if not call_endpoint:
            raise Exception("Method not supported!")
        pr = cProfile.Profile()
        pr.enable()
        # Start
        call_endpoint(endpoint)
        # End
        pr.disable()
        ps = pstats.Stats(pr, stream=io.StringIO()).sort_stats()
        # pr.print_stats()
        print("-".center(title_size, header_fill_char))
        print(" Deterministic Profiling ({}) ".center(title_size, body_fill_char).format(endpoint))
        print("-".center(title_size, header_fill_char))

        print("{}EndPoint:{} {}".center(subtitle_size).format(BOLD, END, endpoint))
        print("{}Total calls:{} {}".center(subtitle_size).format(BOLD, END, ps.total_calls))
        print("{}Total TT:{} {}\n".center(subtitle_size).format(BOLD, END, ps.total_tt))

    def test_main_is_json(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.is_json, False)
        self.assertIn("The API is running..", str(res.data))

    def test_endpoint_hello(self):
        res = self.client.get("/hello/", content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.is_json, True)

        json_data = res.json
        assert 'message' in json_data

    def test_endpoint_time(self):
        self.make_profile_endpoint("/hello", "get")
        self.make_profile_endpoint("/", "get")


if __name__ == '__main__':
    unittest.main()
