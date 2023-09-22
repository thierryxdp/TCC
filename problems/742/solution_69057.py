def substitui(s, x, i):
    """"""
    if i <= len(s):
        s[0:i] + x + s[i]
        return  s[:i] + x + s[i+1:]