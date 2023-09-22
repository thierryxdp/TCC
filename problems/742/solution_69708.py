""" Retorna uma string com o caractere='x' substituindo
o caractere de uma string em uma posicao escolhida"""
def substitui(s,x,i):
    nome = s
    return nome[0:i] + x + nome[i+1:]