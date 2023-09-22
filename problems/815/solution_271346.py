def insere(lista_numero, n):
    '''Dada uma lista de números inteiros em ordem crescente
    e um número inteiro n, inclui n na posição correta
    list, int -> list'''
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    return lista_numero