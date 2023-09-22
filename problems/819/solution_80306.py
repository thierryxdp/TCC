def filtraMultiplos(lista_numeros,n):
    lista = []
    i = 0
    while lista_numeros[i]<len(lista_numeros):
        if lista_numeros[i]%n == 0:
            lista = lista + lista_numeros[i]
        i = i + 1
    return lista