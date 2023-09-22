""" A função retorna uma string, dados uma string(s), um caractere(x) e um número inteiro(i). """
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i] + x + s[i+1]