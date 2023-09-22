def substitui(s,x,i):
    """string, int, int -> string"""
    return s[:i:] + x + s[i + 1:]