def filtraMultiplos(lista,n):
    listanova = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == int:
            listanova = listanova + [lista[proximo],]
        proximo=proximo + 1
    return listanova