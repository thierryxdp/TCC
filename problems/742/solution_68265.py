def substitui(s,x,i):
    '''Função que dada uma string s, um caractere x e um número inteiro i, retorna o caractere x substituido na posição i
    str, str, int -> string'''
    return s[0:i]+x+s[i+1:]