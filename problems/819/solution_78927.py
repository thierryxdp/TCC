def filtra_numeros(lista,n):
    ''''''
    contador = 0
    acumulador = []
    while lista[contador] < len(lista):
        if lista(contador)%n == 0:
            acumulador = acumulador + lista(contador)
    return acumulador