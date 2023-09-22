def substitui(s,x,i):
    '''retorna uma string s, com o caractere x  na posição i:
    str, str, int --> str'''
    frase = s
    return frase[0:i]+x+frase[i+1:-]