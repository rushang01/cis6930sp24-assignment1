import unittest
from  censoror import censor_text

class TestCensorAddresses(unittest.TestCase):
    def test_censor_address_with_pyap(self):
        content = "Send mail to 3538 SW 20th Blvd Apt 09E, Gainesville, FL 32847"
        flags = ['address']
        expected_content = "Send mail to ████████████████████████████████████████████████"
        censored_content = censor_text(content, flags)
        self.assertEqual(censored_content, expected_content)


if __name__ == '__main__':
    unittest.main()

