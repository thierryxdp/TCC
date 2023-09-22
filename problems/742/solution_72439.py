def substitui(s, x, i):
    str(s)[i] = x
    return s[0:i] + x + s[i + 1:]