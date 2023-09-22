'''Programa recebe número inteiro e positivo n e retorna 
a soma de todos os inversos de 1 até o número, com precisão de
duas casas decimais.
int -> int'''
def soma_h(n):
    lista = []
    comprimento = list(range(n + 1))[1:]
    for elemento in comprimento:
        lista = lista + [1/elemento]
    soma = sum(lista)
    return round(soma, 2)