def faltante(lista):
    numeros = len(lista)+1
    for x in range(1, numeros+1):
        if x not in lista:
            return x