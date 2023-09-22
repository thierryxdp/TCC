def substitui(s,x,i):
    '''
    substitui x da string s em posição i.
    str, str, int -> str
    '''
    if 0 <= i < len(s):
    	return s.replace (s[i], x)