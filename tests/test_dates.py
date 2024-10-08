import unittest
from  censoror import censor_text

class TestCensorDates(unittest.TestCase):
    def test_censor_date(self):
        content = "My birthday is on 25th July."
        flags = ['dates']
        expected_content = "My birthday is on █████████."
        censored_content = censor_text(content, flags)
        self.assertEqual(censored_content, expected_content)

if __name__ == '__main__':
    unittest.main()
