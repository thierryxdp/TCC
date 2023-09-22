#list -> list
def insere(lista_numero,n):
    "função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada"
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero