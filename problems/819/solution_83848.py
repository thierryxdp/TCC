def filtraMultiplos(lista, n):
    listaFinal = []
    for num in lista:
        if(num % n == 0):
            listaFinal.append(num)
    return listaFinal