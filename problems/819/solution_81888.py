def filtraMultiplos(numeros, n):
    lista = []
    i = 0
    while i in numeros:
        if type(numeros[i]/n)=='int':
            lista = lista.append(numeros[i])
            i+=1
    return lista