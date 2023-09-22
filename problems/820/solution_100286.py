def posLetra(s, l, n):
    '''Função que conta uma letra que aparece em determinada ocorrência
    str, str, int--> int'''
    
    palavras = list(s)
    c = 0
    o = 0
    while len(palavras) > c:
        if l in palavras[c]:
            o += 1
            if o == n:
                return c
        c += 1
    if o < n:
        return -1
    else:
        return o