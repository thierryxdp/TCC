"""Dados uma string "s", um carctere "x" e um número
inteiro "i" entre o e o comprimento da string, retorna
uma string igual a "s" mas com o elemento da posição "i"
sendo substituído por "x"
string, int, int -> string"""
def substitui(s,x,i):
    return s[:i] + x + s[i+1:]