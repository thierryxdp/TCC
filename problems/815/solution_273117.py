def insere(lista_numero, n):
    """
    Essa função recebe uma lista ordenada crescente de inteiros
    e um número n, retornando uma lista ordenada com esses números
    e n;
    list, int -> list
    """
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero