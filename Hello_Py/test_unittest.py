import Incr_Desc    # The code to test
import unittest   # The test framework


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(Incr_Desc.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(Incr_Desc.decrement(3), 4)


if __name__ == '__main__':
    unittest.main()