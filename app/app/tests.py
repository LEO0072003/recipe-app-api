from django.test import SimpleTestCase
from .import calc

class Calctest(SimpleTestCase):
    def test_add(self):
        res = calc.add(5,6)
        self.assertEqual(res , 11)
    def test_subs(self):
        res = calc.subs(5,6)
        self.assertEqual(abs(res) , 1)