def filtraMultiplos(ls, n):
    """A função recebe uma lista e um número e retorna uma lista coms números divisíveis por n da primeira lista.
    assinatura: list->list"""
    lista = []
    for x in ls:
        if x%n==0:
            lista.append(x)
    return lista