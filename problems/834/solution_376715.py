def media_matriz(matriz):
    numeros = ()
    for i in matriz:
        for j in i:
        	numeros = numeros + (j,)
    return sum(numeros)/len(numeros)