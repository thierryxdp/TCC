def substitui(s,x,i):
    '''
    substitui x da string s em posição i.
    str, int, int -> str
    '''
    if 0 <= i <= len(str(s)):
        return s.replace (s[i], str(x))