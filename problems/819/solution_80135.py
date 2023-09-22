def filtraMultiplos(lista, n):
    w=0
    aux=[]
    while w < len(lista) :
        if lista[w]%n==0:
            aux= aux + lista[w]
        w=w+1
    return aux