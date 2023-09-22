def insere(lista_numero, n):
    '''Código que forma uma lista crescente, para os números maiores que n
    lista, int -> int'''
    list(lista_numero)
    lista_numero.append(n)
    lista_ordenada = sorted(lista_numero)
    return lista_ordenada