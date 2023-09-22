def insere(lista_numero, n):
    '''Dada uma lista de numeros em ordem crescente (lista_numero) e um numero n, a funcao retorna a lista com a adicao de n ainda de forma ordenada.
List, int -> list.'''
    lista_numero_copia = lista_numero[:]
    list.append(lista_numero_copia, n)
    list.sort(lista_numero_copia)
    return lista_numero_copia