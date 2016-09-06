import parser_sc
from basic.read_char import *
from color import *


def onclick():
    pass


def get_lex_type(ch):
    if ch.isalpha() or ch == '_':
        return "identifier"
    elif ch.isdigit():
        return "digit"


def get_token(f, ch):
    ch = parser_sc.pre_process(f, ch)
    lex_type = get_lex_type(ch)

    if lex_type == 'identifier':
        set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        word = parser_sc.parse_identifer(f, ch)
        sys.stdout.write(word)
        sys.stdout.flush()
        reset_color()
    ch = get_ch(f)
    return ch


if __name__ == "__main__":
    f = open("C:\\test.sc", "r")
    ch = get_ch(f)
    k = 0
    while ch != '':
        ch = get_token(f, ch)
        k += 1
    f.close()
