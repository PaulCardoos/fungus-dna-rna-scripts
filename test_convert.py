import unittest
from utils import convert, organize_data, read_csv, sort_dict_vals
class TestUtils(unittest.TestCase):
    def test_convert(self):

        some_data = read_csv("/Users/mirna/fungus-code/fungai-data.csv")
        aa = organize_data(some_data)
        aa = sort_dict_vals(aa)

        self.assertEquals(convert("GAGAACTCGAGCTTAGTGCCCTGA", aa), "GAGAACTCCTCCCTCGTCCCCTAA")
        self.assertEquals(convert("TTTTCGTACATTACCGCCGATTGA", aa), "TTCTCCTACATCACCGCCGACTAA")