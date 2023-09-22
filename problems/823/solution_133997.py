def faltante(lista):
    """ Recebe uma lista numérica de entrada e retorna o numéro que está faltando na lista;
    list->int """
    list.sort(lista)
    x=lista[0]
    y=lista[-1]+1
    i=0
    if 1 not in lista:
        return 1
    if lista==list(range(x,y)):
        return y
    while lista[i]==list(range(x,y))[i]:
            i=i+1
    return i+1