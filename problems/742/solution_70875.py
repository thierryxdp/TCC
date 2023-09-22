"""Substitui, na palavra S, a letra na posição I pela letra "X"
Palavra S, posição I, letra X
string, string, int -> string"""
def substitui(s,x,i):
    return parte1(s,i) + str(x) + parte2(s,i)
def parte1(s,i):
    return s[0:i]
def parte2(s,i):
    return s[i+1:]