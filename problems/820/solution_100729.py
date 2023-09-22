def posLetra(frase,l,n):
    """ função que retorna a posição que ocorre certa letra
    str, str, int"""
    i = 0
    p = 0
    while i < len(frase):
        p = str.find(frase,l,n,i)
        i = i + 1
    return p