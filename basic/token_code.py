from enum import Enum
Token_Code = Enum('Token_Code', ('TK_INVALID','TK_PLUS', 'TK_MINUS', 'TK_STAR', 'TK_DIVIDE', 'TK_MOD',
                                     'TK_EQ', 'TK_NEQ', 'TK_LT', 'TK_LEQ', 'TK_GT',
                                     'TK_GEQ', 'TK_ASSIGN', 'TK_POINTSTO', 'TK_DOT', 'TK_AND',
                                     'TK_OPENPA', 'TK_CLOSEPA', 'TK_OPENBR', 'TK_CLOSEBR', 'TK_BEGIN',
                                     'TK_END', 'TK_SEMICOLON', 'TK_COMMA', 'TK_ELLIPSIS', 'TK_EOF',
                                     'TK_CINT', 'TK_CCHAR', 'TK_CSTR', 'KW_CHAR', 'KW_SHORT',
                                     'KW_INT', 'KW_VOID', 'KW_STRUCT', 'KW_IF', 'KW_ELSE',
                                     'KW_FOR', 'KW_CONTINUE', 'KW_BREAK', 'KW_RETURN', 'KW_SIZEOF',
                                     'KW_ALIGN', 'KW_CDECL', 'KW_STDCALL', 'TK_IDENT'))


