def filtraMultiplos(lista_numeros,n):
    lista = []
    i = 0
    while i<len(lista_numeros):
        if lista_numeros[i]%n == 0:
        lista = lista + lista_numeros[i]
    i = i + 1
    return len(lista_numeros)