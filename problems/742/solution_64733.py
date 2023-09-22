"""Funcao que substitui e recebe uma string s, caractere x e um numero int
string, int, int -> string"""
def substitui(s,x,i):
    #i == len (s)
    return s[0:i-1]+ x + s[i+1]