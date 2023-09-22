def filtraMultiplos(lista_numeros,n):
    lista_numeros =list(lista_numeros)
    i=0
    numeros=()
    while i<len(lista_numeros):
        if lista_numeros[i]%n == 0:
            numeros = numeros + (lista_numeros[i],)
        i = i + 1
    return numeros