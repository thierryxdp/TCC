def substitui(s,x,i):
    """substitui o termo i da string s pela letra x;
    str, str, int -> str"""
    return s[0:(i)] + x + s[(i+1):]