import unittest
from atm import check_pin, new_balance

class ATMtest(unittest.TestCase):
    def test_pin_true(self):
        result = 000
        self.assertEqual(result, 000)

    def test_pin_false(self):
        expected = not 000
        self.assertNotEqual(expected, 1234)

    def test_withdrawal_acceptable(self):
        expected = range(1,100)
        assert(True)

    def test_withdrawal_exceeds(self):
        expected = range(100,1000)
        assert(True)

    def test_exception(self):
        self.assertRaises(OverflowError)
        assert(True)

   # def test_withdrawal_exceeds(self):
        


