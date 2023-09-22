def insere(lista_numero: list, n: int) -> list:
    '''Dada uma lista ordenada e um número, devolve 
    nova lista ordenada contendo o número'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero