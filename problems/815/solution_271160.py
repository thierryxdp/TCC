def insere(lista_numero, n):
    '''Dada uma lista de numeros em ordem crescente (lista_numero) e um numero n, a funcao retorna a lista com a adicao de n ainda de forma ordenada.
List, int -> list.'''
    lista_com_n = list.append(lista_numero, n)
    return list.sort(lista_com_n)