import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Test for city_functions"""

    def test_city_functions(self):
        """Do you get the correct result?"""
        formatted_city = city_country("london", "england")
        self.assertEqual(formatted_city, "London, England - Population 50000")


if __name__ == '__main__':
    unittest.main()
