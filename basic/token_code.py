import collections
token_code = collections.namedtuple("tokenCode", 
	('TK_PLUS', 'TK_MINUS', 'TK_STAR','TK_DIVIDE', 'TK_MOD', 
		'TK_EQ',   'TK_NEQ',   'TK_LT',   'TK_LEQ',   'TK_GT', 
		'TK_GEQ',  'TK_ASSIGN', 'TK_POINTSTO', 'TK_DOT', 'TK_AND',
		'TK_OPENPA', 'TK_CLOSEPA','TK_OPENBR', 'TK_CLOSEBR', 'TK_BEGIN', 
		'TK_END', 'TK_SEMICOLON', 'TK_COMMA', 'TK_ELLIPSIS', 'TK_EOF', 
		'TK_CINT', 'TK_CCHAR', 'TK_CSTR','KW_CHAR', 'KW_SHORT',
		'KW_INT', 'KW_VOID', 'KW_STRUCT', 'KW_IF', 'KW_ELSE',
		'KW_FOR', 'KW_CONTINUE', 'KW_BREAK', 'KW_RETURN', 'KW_SIZEOF',
		'KW_ALIGN', 'KW_CDECL', 'KW_STDCALL', 'TK_IDENT'))

token_codes = token_code(0,1,2,3,4,5,6,7,8,9,10,
	11,12,13,14,15,16,17,18,19,20,21,22,
	23,24,25,26,27,28,29,30,31,32,33,34,
	35,36,37,38,39,40,41,42,43)