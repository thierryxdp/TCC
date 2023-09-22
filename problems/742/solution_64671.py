string, int, int -> string
def substitui(s,x,i):
    '''funcao que receba uma string s, um caractere x e um numero inteiro i e retorne uma string igual a s'''
    return s[0:i] + s[i+1]