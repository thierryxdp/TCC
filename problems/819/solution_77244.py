def filtraMultiplos(lista,n):
    retorno=()
    a=len(lista)
    for i in range(a):
        if lista(i)%n==0:
            retorno=retorno+(lista[i],)
    return retorno