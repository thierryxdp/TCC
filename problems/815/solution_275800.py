def insere(lista_numero, n):
    """
    funcao que dada uma lista ordenada (crescente) de numeros
    inteiros e um numero n, reorganiza a lista colocando o n
    na posição correta, de forma que a lista continue ordenada.
    :param lista_numero: list 
    :param n: int 
    :return: list 
    """
    list(lista_numero)
    lista_numero.append(n)
    lista_ordenada = sorted(lista_numero)

    return lista_ordenada