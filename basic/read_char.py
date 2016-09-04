def get_ch(f):
    return f.read(1)


def unget_ch(f):
    k = f.tell()
    f.seek(k - 1, 0)


def cur_pos(f):
    return f.tell()


def read_to_buffer(f, begin, end):
    buf = ''
    f.seek(begin)
    buf = f.read(end - begin)
    return buf
