'''Adiciona um número a uma lista ordenada de números, de forma que mantenha
a sua ordenação
list -> list'''
def insere(lista_numero, n):
    lista_numero += [n]
    lista_numero.sort()
    return lista_numero