import unittest
from app import app

class TestPalindromeChecker(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Palindrome Checker', response.data)

    def test_palindrome_check(self):
        response = self.app.post('/', data={'string': 'level'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The string is a palindrome', response.data)

        response = self.app.post('/', data={'string': 'hello'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The string is not a palindrome', response.data)

if __name__ == '__main__':
    unittest.main()
