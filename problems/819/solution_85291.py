def filtraMultiplos(lista, n):
    lista2 = []
    x=0
    while x < lista:
        if lista[x]%n==0:
            lista2.append(lista[x])
        x+=1
    return lista2