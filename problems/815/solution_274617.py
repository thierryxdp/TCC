def insere(lista_numero, n):
    '''dada uma lista em ordem crescente, adiciona um numero n em sua respectiva posição;
    list, int -> list'''
    lista = lista_numero + [n]
    list.sort(lista)
    return lista