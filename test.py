from unittest import TestCase, main
import stringindex as si
from pprint import PrettyPrinter


class TestStringIndex(TestCase):
    def test_parse_string(self):
        scenario = {
            'filters[1][field]': ['year'],
            'filters[1][operator]': ['btw'],
            'filters[1][value][0]': ['2020'],
            'filters[1][value][1]': ['2021'],
            'filters[0][field]': ['month'],
            'filters[0][operator]': ['btw'],
            'filters[0][value][0]': ['8'],
            'filters[0][value][1]': ['9'],
            'orders[date]': ['asc'],
        }

        result = si.parse(scenario)
        pp = PrettyPrinter()
        pp.pprint(result)


if __name__ == '__main__':
    main()
