'''Programa recebe uma lista de números inteiros e um número n inteiro.
Função insere o número n na lista e os organiza em ordem crescente.
list, int -> list'''
def insere(lista_numero, n):
    lista0 = list.insert(lista_numero, 0, n)
    lista1 = list.sort(lista_numero)
    return lista_numero