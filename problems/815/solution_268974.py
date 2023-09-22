def insere(lista_numero, n):
    """A função recebe uma lista ordenada de numeros inteiros e um numero
    inteiro n, que é incluido na lista, de forma a continuar mantendo ela
    ordenada;
    list, int -> list"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero