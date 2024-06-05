import unittest
import challenge_3

class TestFormatPhoneNumber(unittest.TestCase):

    def test_valid_phone_number(self):
        self.assertEqual(challenge_3.format_phone_number("(555) 111-2222"), "(555) 111-2222")
        self.assertEqual(challenge_3.format_phone_number("(555) 1234567"), "(555) 123-4567")
        self.assertEqual(challenge_3.format_phone_number("555 222-2222"), "(555) 222-2222")
        self.assertEqual(challenge_3.format_phone_number("555-333 4444"), "(555) 333-4444")
        self.assertEqual(challenge_3.format_phone_number("555 666 7777"), "(555) 666-7777")
        self.assertEqual(challenge_3.format_phone_number("4556660777"), "(455) 666-0777")

if __name__ == '__main__':
    unittest.main()
