"""
Sample tests
"""

from django.test import SimpleTestCase
from rest_framework.test import APIClient


class ViewTests(SimpleTestCase):
    # def test_add_numbers(self):
    #     res = calc.add(5,6)
    #     self.assertEqual(res, 11)

    # def test_subtract_numbers(self):
    #     res = calc.subtract(10,15)
    #     self.assertEqual(res, 5)

    def test_get_greetings(self):
        client = APIClient()
        res = client.get("/admin/")

        self.assertEqual(res.status_code , 302)
        #self.assertEqual(res.data, [])