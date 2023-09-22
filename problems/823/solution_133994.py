def faltante(lista):
    """ Recebe uma lista numérica ordenada de entrada e retorna o numéro que está faltand na lista;
    list->int """
    x=lista[0]
    y=lista[-1]+1
    i=0
    while lista[i]==list(range(x,y))[i]:
            i=i+1
    return i+1