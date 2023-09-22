def filtraMultiplos(numeros, n):
    lista = []
    i = 0
    while i in numeros:
        if type(numeros[i]/n)=='int':
            lista = numeros.append(i)
            i+=1
    return lista