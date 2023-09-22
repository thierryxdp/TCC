def filtraMultiplos(listaNumeros,n):
    """Dada uma lista de números e um número n, a função
    retorna uma lista que contém todos elementos da lista
    original divisíveis por n.
    Parametros de Entrada: list, int
    Retorna: lis"""

    i=0
    lista=[]

    while i< len(listaNumeros):
        if (listaNumeros[i]%n)==0:
            lista= lista + [listaNumeros[i]]
        i=i+1
    return lista