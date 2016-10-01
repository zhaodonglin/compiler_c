from parser_sc import *
from basic.read_char import *
from color import *
import sys
from basic.token_code import *

token_type_map_without_next_char = {
    "+": Token_Code.TK_PLUS,
    "/": Token_Code.TK_DIVIDE,
    "%": Token_Code.TK_MOD,
    ".": Token_Code.TK_DOT,
    "&": Token_Code.TK_AND,
    "(": Token_Code.TK_OPENPA,
    ")": Token_Code.TK_CLOSEPA,
    "[": Token_Code.TK_OPENBR,
    "]": Token_Code.TK_CLOSEBR,
    "{": Token_Code.TK_BEGIN,
    "}": Token_Code.TK_END,
    ";": Token_Code.TK_SEMICOLON,
    ",": Token_Code.TK_COMMA

}

token_type_map_with_next_char = {
    "-": ['>', Token_Code.TK_PLUS, Token_Code.TK_POINTSTO],
    "=": ['=', Token_Code.TK_ASSIGN, Token_Code.TK_EQ],
    '<': ['=', Token_Code.TK_LT, Token_Code.TK_LEQ],
    '>': ['=', Token_Code.TK_GT, Token_Code.TK_GEQ],
    '!': ['=', Token_Code.TK_INVALID, Token_Code.TK_NEQ]
}


def get_lex_type(f, ch):
    token_type = token_type_map_without_next_char.get(ch)
    if token_type is not None:
        return ch, token_type
    token_get_paratmeter = token_type_map_with_next_char.get(ch)
    if token_get_paratmeter is not None:
        return parse_with_next_char(f, ch,
                                    token_get_paratmeter[0],
                                    token_get_paratmeter[1],
                                    token_get_paratmeter[2])
    if ch.isalpha() or ch == '_':
        return parse_identifer(f, ch)
    if ch.isdigit():
        return parse_number(f, ch)
    if ch == "\"":
        return parse_string(f)
    else:
        return "unkown", Token_Code.TK_INVALID


def get_token(f, ch):
    first_not_separate_char = pre_process(f, ch)
    word, token_type= get_lex_type(f, first_not_separate_char)
    reset_color()

    if token_type == Token_Code.TK_IDENT:
        set_cmd_color(FOREGROUND_BLUE)
    elif token_type == Token_Code.TK_BEGIN or token_type == Token_Code.TK_END:
        set_cmd_color(FOREGROUND_GREEN)
    elif token_type in keyword_map.values():
        set_cmd_color(FOREGROUND_RED)
    else:
        reset_color()
    print(word, end="", flush=True)
    next_char = get_ch(f)
    return next_char


if __name__ == "__main__":
    f = open("C:\\test.sc", "r")
    ch = get_ch(f)
    k = 0
    while ch != '':
        ch = get_token(f, ch)
        k += 1
    f.close()
