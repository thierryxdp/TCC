def filtraMultiplos(lista,n):
    multi = []
    contador = 0
    while contador<len(lista):
        if lista[contador]%n==0:
            list.append(multi,lista[contador])
        contador = contador + 1
    return multi