"""Função que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x.
string, int, int -> string"""
def substitui(s,x,i):
    return s[:i] + x + s[i:]