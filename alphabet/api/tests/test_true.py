import string

from rest_framework.test import APITestCase


class TrueTestCase(APITestCase):
    """
    APITestCase class to handle all expected True inputs
    """
    
    def test_true(self):
        data = {
            "request": string.ascii_lowercase
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], True)

    def test_true_alphanumberic(self):
        data = {
            "request": "a86bcde23458fghijk8lmno83568pqrstuv4848wx4yz"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], True)

    def test_true_special_chars(self):
        data = {
            "request": "abc@&@*def*(#)g()&hijklmnopqrstu(@&#&$vwx@)@)%yz!@#$%^&*()\"_+-=[{]}\|';/?.><,`~"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], True)

    def test_true_all_chars(self):
        data = {
            "request": "a!@$bcde*#*1761fgh@#^@#^473ijklmnopqrs27t1^@#^7272uvwx*%#yz`1234567890-=~!@#$%^&*()_+[{]}\|'\";:,./<>?"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], True)

    def test_true_sentence(self):
        data = {
            "request": "The quick brown fox jumps over the lazy dog 38 times!"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], True)

    def test_true_book(self):
        data = {
            "request": "Lorem ipsum dolor sit amet, consectetur adipiscing \
            elit, sed do eiusmod tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco \
            laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
            in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla \
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa \
            qui officia deserunt mollit anim id est laborum jwkzy"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], True)