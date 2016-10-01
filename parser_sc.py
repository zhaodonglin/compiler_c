import unittest
from basic.read_char import *
from basic.create_file_for_test import *
from basic.token_code import *

line_num = 1


class ParserTest(unittest.TestCase):
    _str = "   I love you"
    file_name = "C:\\skip_white_space.txt"

    def setUp(self):
        create_file_for_test(self.file_name, self._str)

    def tearDown(self):
        pass

    def test_skip_white_space(self):
        f = open(self.file_name, "r")
        ch = get_ch(f)
        ch = skip_white_space(f, ch)
        self.assertEqual(ch, 'I')
        f.close()

    def test_skip_white_space_first_char_is_not_white_space(self):
        self._str = "I love you"
        self.file_name = "C:\\skip_white_space.txt"
        create_file_for_test(self.file_name, self._str)
        f = open(self.file_name, "r")
        ch = get_ch(f)
        ch = skip_white_space(f, ch)
        self.assertEqual(ch, 'I')
        f.close()

    def test_parse_comment(self):
        self._str = "/*I love you*/"
        self.file_name = "C:\\parse_comment.txt"
        create_file_for_test(self.file_name, self._str)
        f = open(self.file_name, "r")
        ch = get_ch(f)
        ch = parse_comment(f)
        self.assertEqual(ch, '')
        f.close()

    def test_parse_comment_with_an_alpha_in_the_end(self):
        self._str = "/*I love you*/a"
        self.file_name = "C:\\parse_comment.txt"
        create_file_for_test(self.file_name, self._str)
        f = open(self.file_name, "r")
        ch = get_ch(f)
        ch = parse_comment(f)
        self.assertEqual(ch, 'a')
        f.close()

    def test_parse_comment_no_end_flag(self):
        self._str = "/*I love you"
        self.file_name = "C:\\parse_comment.txt"
        create_file_for_test(self.file_name, self._str)
        f = open(self.file_name, "r")
        ch = get_ch(f)
        ch = parse_comment(f)
        self.assertEqual(ch, 'no')
        f.close()

    def test_parse_comment_with_two_lines(self):
        self._str = "/*I love you\r\n hell*/"
        self.file_name = "C:\\parse_comment.txt"
        create_file_for_test(self.file_name, self._str)
        f = open(self.file_name, "r")
        ch = get_ch(f)
        ch = parse_comment(f)
        self.assertEqual(ch, '')
        f.close()


def skip_white_space(f, ch):
    global line_num
    while ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n':
        if ch == '\r':
            ch = get_ch(f)
            if ch != '\n':
                return ch
            line_num += 1
        elif ch == '\n':
            line_num += 1
        print(ch, end="")
        ch = get_ch(f)
    return ch


def parse_comment(f):
    global line_num
    ch = get_ch(f)
    while True:
        while True:
            if ch == '\n' or ch == '*' or ch == '':
                break
            else:
                ch = get_ch(f)
        if ch == '\n':
            line_num += 1
            ch = get_ch(f)
        elif ch == '*':
            ch = get_ch(f)
            if ch == '/':
                ch = get_ch(f)
                return ch
        else:
            print("no end of comments until the end of file")
            return "no"


def pre_process(f, ch):
    while True:
        if ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n':
            ch = skip_white_space(f, ch)
        elif ch == '/':
            ch = get_ch(f);
            if ch == '*':
                ch = parse_comment(f)
            else:
                unget_ch(f)
                ch = '/'
                break
        else:
            break
    return ch


def parse_identifer(f, ch):
    identifier = ""
    while ch.isdigit() or ch.isalpha() or ch == '_':
        identifier = identifier + ch
        ch = get_ch(f)
    unget_ch(f)
    return identifier, Token_Code.TK_IDENT


def parse_string(f):
    string = ""
    nxt_ch = get_ch(f)
    while nxt_ch != "\"":
        string += nxt_ch
        nxt_ch = get_ch(f)
    return string, Token_Code.TK_CSTR


def parse_number(f, ch):
    identifier = ""
    while ch.isdigit():
        identifier = identifier+ch
        ch = get_ch(f)
    unget_ch(f)
    return identifier, Token_Code.TK_CINT


def parse_with_next_char(f, firstchar, nextchar, first_token, next_token):
    ch = get_ch(f)
    if ch == nextchar:
        return firstchar+nextchar, next_token
    else:
        unget_ch(f)
        return firstchar, first_token

if __name__ == '__main__':
    unittest.main()
