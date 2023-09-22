"""Função que recebe uma string s, um caratere x e 
um número inteiro i (entre o e o comprimento da string)
e retorna uma string s substituindo um elemento da posição i pelo caractere x.
Assinatura: string, int, int -> string
Testes:
substitui('manga', 'o', 4) == 'mango'
substitui('Lima', 'o', 3) == 'Limo'
"""
def substitui(s,x,i):
    n = i + 1
    return s[ : i] + x + s[n: ]