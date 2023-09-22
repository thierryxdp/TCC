def repetidos(lista):
    contador = 0
    n = 0
    while contador < len(lista)-1:
        numeros = list(zip(lista[contador+1], lista[contador]))
        if numeros[0] == numeros[1]:
            n = n + 1                 
    return n