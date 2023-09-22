'''Essa função que retorna uma string dado uma string s, um caractere x e um numero inteiro entre 0
string, int, int -> string'''
def substitui(s,x,i):
    return (str(s)[0:i])+str(x)+(str(s)[i+1:])