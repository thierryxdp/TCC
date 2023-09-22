def filtraMultiplos(numeros, n):
    lista = []
    for i in numeros:
        if type(i/n)=='int':
            lista = numeros.append(i)
    return lista