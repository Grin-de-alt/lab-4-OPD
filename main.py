import unittest
from app import app

class TestConversion(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_conversion_calculation(self):
        data = {'amount': '10', 'from_c': 'USD', 'to_c': 'EUR'}
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Euro', response.data)

    def test_bad_request(self):
        data = {'amount': '10', 'from_c': 'ZWL', 'to_c': 'EUR'}
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bad Request', response.data)
        if __name__ == '__main__':
            unittest.main()
