def filtraMultiplos(lista, n):
    cont = 0
    lista2 = []
    while (cont<len(lista)):
        if lista[cont]%n == 0:
            lista2.append(lista[cont])
        cont = cont + 1
    return lista2