def posLetra(frase,l,n):
    """ função que retorna a posição que ocorre certa letra
    str, str, int"""
    i = 0
    p = []
    while len(frase)>i:
        if str.find(frase,l) == -1:
            return -1
        elif frase[i] == l:
            p = p + [i]
        i = i + 1
    if len(p)<n:
        return -1
    else:
        return p[n-1]