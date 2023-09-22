def insere(lista_numero,n):
    'Dada uma lista com números inteiro, incluir n de maneira que continue ordenada. Entradas: list[inteiros], int. Saídas: list[inteiros].'
    lista_numero=lista_numero+[n]
    return sorted(lista_numero)