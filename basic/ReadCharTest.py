import unittest
from basic.read_char import get_ch, unget_ch
from basic.create_file_for_test import create_file_for_test


class ReadCharTest(unittest.TestCase):
    file_name = "C:\\read_char.txt"
    _str = "I love you"

    def setUp(self):
        create_file_for_test(self.file_name, self._str)

    def tearDown(self):
        pass

    def test_get_ch(self):
        f = open(self.file_name, "r")
        ch = get_ch(f)
        self.assertEqual(ch, 'I')
        ch = get_ch(f)
        self.assertEqual(ch, " ")
        f.close()

    def test_unget_ch(self):
        f = open(self.file_name, "r")
        ch = get_ch(f)
        self.assertEqual(ch, 'I')
        unget_ch(f)
        ch = get_ch(f)
        self.assertEqual(ch, 'I')
        f.close()


if __name__ == "__main__":
    unittest.main()
