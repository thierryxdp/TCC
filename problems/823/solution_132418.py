def faltante(lista):
    numeros = len(lista)
    for x in range(0, numeros):
        if x not in lista:
            return x