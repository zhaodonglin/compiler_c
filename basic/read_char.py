def get_ch(f):
	return f.read(1)

def unget_ch(f):
	k = f.tell()
	f.seek(k-1,0)