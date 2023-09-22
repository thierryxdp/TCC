def substitui(s, x, i):
    '''Recebe uma string s, um caractere x e um numero i, substitui a posicao i na string s pelo caractere x
    str, str, int -> str'''
    return s[:i] + str(x) + s[i+1:]