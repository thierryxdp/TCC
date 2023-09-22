def posLetra(s,l,n):
    '''retorna em que posiçao da string s a ocorrencia da letra l esta'''
    '''str, str, int -> int'''
    
    pos = s.find(l)
    
    while pos >= 0 and n > 1:
        pos = s.find(l, pos + 1)
        n -= 1
    return pos