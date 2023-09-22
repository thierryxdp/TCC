def insere (lista_numero: list, n: int)-> list:
    '''Dada uma lista de números inteiros crescentes e um número
    inteiro n, retorna uma lista com n incluido na posição correta'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero