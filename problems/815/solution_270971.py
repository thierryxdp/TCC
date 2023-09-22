def insere(lista_numero: list, n: int):
    """Essa função, dada uma lista ordenada de números inteiros e
    um número inteiro n, insere o númeri n na lista de maneira que
    continue ordenada"""
   	
    lista_numero += [n,]
    lista_numero.sort()
    return lista_numero