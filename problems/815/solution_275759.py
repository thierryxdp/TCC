def insere(lista_numero, n):
    """funcao que dada uma lista ordenada crescente de numeros inteiros e um numero n, retorna
    o numero n na posição correta, de tal maneira que a lista continue ordenada;
    list, int --> list"""
    lista_numero[2:2] = [n]
    organizado = list.sort(lista_numero)
    return organizado