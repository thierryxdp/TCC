def faltante(lista):
    numeros = len(lista)
    for x in range(1, numeros+1):
        if x not in lista:
            return x