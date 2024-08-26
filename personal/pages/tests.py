from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        self.response = self.client.get("/")
        self.assertEqual(self.response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        self.response = self.client.get("/about/")
        self.assertEqual(self.response.status_code, 200)