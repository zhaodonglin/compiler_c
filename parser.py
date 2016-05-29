
import unittest
from basic.read_char import *

def skip_white_space(f,ch):
	while(ch == ' ' or ch=='\t' or ch=='\r'):
		if ch=='\r':
			ch=getch(f)
			if ch!='\n':
				return ch
			line_num = line_num + 1
		ch = get_ch(f)
	return ch

def parse_comment(f):
	ch = get_ch(f)
	while(True):
		while(True):
			if ch=='\n' or ch == '*' or ch== '':
				break
			else:
				ch=get_ch(f)
		if ch=='\n':
			line_num = line_num + 1
		elif ch=='*':
			ch=get_ch(f)
			if ch =='/':
				ch= get_ch(f)
				return ch
		else:
			print ("no end of comments untill the end of file")
			return ch

def pre_process(f,ch):
	while(True):
		if (ch==' ' or ch=='\t' or ch=='\r'):
			ch=skip_white_space(f,ch)
		elif (ch == '/'):
			ch=get_ch(f);
			if (ch=='*'):
				parse_comment(f)
			else:
				unget_ch(f)
				ch='/'
				break
		else:
			break

def parse_identifer(f,ch):
	identifier =""
	while (ch.isdigit() or ch.isalpha()):
		identifier = identifier + ch
		ch = get_ch(f)
	return identifier

# if __name__ == '__main__':
# 	f = open("C:\\1.txt","r")
# 	# while(True):
# 	# 	ch=get_ch(f)
# 	# 	print(ch)
# 	# 	if ch == '':
# 	# 		print ("end of file")
# 	# 		break

# 	# ch=skip_white_space(f,ch)
# 	# print(ch)
# 	ch = get_ch(f)
# 	pre_process(f,ch)
# 	word = parse_identifer(f,ch)
# 	print(word)
# 	f.close()





