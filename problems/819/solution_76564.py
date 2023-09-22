def filtraMultiplos(lista_numeros,n):
    lista_numeros = []
    for n in lista_numeros:
        if n/lista_numeros:
            lista_numeros.append(n)
    return lista_numeros