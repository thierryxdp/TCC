def filtraMultiplos(numeros,multiplo):
    listamultiplos = []
    contador = 0
    while contador < len(numeros):
        if numeros[contador] % multiplo == 0:
            list.append(listamultiplos,numeros[contador])
        	contador = contador + 1
    return listamultiplos