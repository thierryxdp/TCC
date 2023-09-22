def insere(lista_numero,n):
    'Dada uma lista com números inteiro, incluir n de maneira que continue ordenada. Entradas: list[inteiros], int. Saídas: list[inteiros].'
    lista_numero[0:0]=n
    return list.sort(lista_numero)