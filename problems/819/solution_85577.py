def filtraMultiplos(lista,n):
    """ list, float -> list;
    Função que recebe uma lista de números e um número n,
    e retorna outra lista contendo os elementos da lista
    inicial que forem divisíveis por n."""
    ret = []
    for e in lista:
        if e // n == True:
            ret.append(e)
    return ret