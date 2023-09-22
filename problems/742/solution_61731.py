def substitui(s,x,i):
    s = s[0:i] + x + s[i + 1:]
    if s[0:i] + x + s[i + 1:]:
        return s
    else:
        return s