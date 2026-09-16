import unittest


class TestSample(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_string(self):
        self.assertEqual("jenkins".upper(), "JENKINS")


if __name__ == "__main__":
    unittest.main()
