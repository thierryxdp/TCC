"""Essa função adiciona um número "n" (inteiro qualquer) em uma lista já ordenada "lista_numero" de tal maneira que a lista continue ordenada mesmo contendo o novo número
Assinatura: List,int -> list"""

def insere(lista_numero,n):
    lista_1 = lista_numero
    lista_2 = list.append(lista_1,n)
    lista_3 = list.sort(lista_1)
    return (lista_1)