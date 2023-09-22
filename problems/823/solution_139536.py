def faltante(lista):
    cont=0
    N=max(lista)
    inteiros=range(1,N+1)
    while cont<len(inteiros):
        if inteiros[cont] not in lista:
            return inteiros[cont]
        cont=cont+1