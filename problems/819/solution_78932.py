def filtraMultiplos(lista,n):
    ''''''
    contador = 0
    acumulador = []
    while contador < len(lista):
        if lista[contador] % n == 0:
            list.append(acumulador, lista[contador])
        contador = contador + 1
    return acumulador