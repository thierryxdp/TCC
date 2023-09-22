def media_matriz(matriz):
    numeros = ()
    for i in matriz:
        for j in i:
        	numeros = numeros + (j,)
    media = round(sum(numeros)/len(numeros), 2)
    return media