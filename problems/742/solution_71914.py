"""Recebe uma string, um caractere e um numero inteiro; e retorna uma string igual a inicial, mas o elemento da posicao do numero inteiro sera substituido pelo caractere escolhido"
assinatura: string, int, int -> string"""
def substitui(s,x,i):
    return s[0:i] + x + s[i+1:]