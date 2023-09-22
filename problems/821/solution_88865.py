def fatorial(numero):
    '''sfsd'''
    lista_numero= list(range(numero+1))
    list.remove(lista_numero,0)
    fatorial=1
    indice=0
    while indice<len(lista_numero):
        fatorial=fatorial*lista_numero[indice]
        indice=indice+1
    return fatorial