def substitui(s,x,i):
    """string, int, int -> string"""
    s[i] = x
    return s[:i:] + x + s[i + 1:]