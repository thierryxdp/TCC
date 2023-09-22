def substitui(s,x,i):
    '''Faz uma string s que contenha o caractere x na posição i'''
    return s[:i-1]+str(x)+s[i:]