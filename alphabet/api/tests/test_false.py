from rest_framework.test import APITestCase


class FalseTestCase(APITestCase):
    """
    APITestCase class to handle all expected False inputs
    """

    def test_false(self):
        data = {
            "request": "abc"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)
    
    def test_false_alphanumeric(self):
        data = {
            "request": "vI0pajIMvdSjOfhcUuO1f5k9CEcbijd"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)

    def test_false_special_chars(self):
        data = {
            "request": "L&fqmez^WoM!ZghBcExB^XptQd^*pkQ"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)

    def test_false_all_chars(self):
        data = {
            "request": "&fSg44WPgG0zpKYeB*e1SQm6ZFOOj6m"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)

    def test_false_sentence(self):
        data = {
            "request": "The qu1ck brown fox jump$ ov3r the lazy d0g!"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)

    def test_false_book(self):
        data = {
            "request": "Lorem ipsum dolor sit amet, consectetur adipiscing \
            elit, sed do eiusmod tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco \
            laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
            in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla \
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa \
            qui officia deserunt mollit anim id est laborum"
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)

    def test_false_blank(self):
        data = {
            "request": ""
        }
        response = self.client.post("", data)
        self.assertEqual(response.json()["response"], False)