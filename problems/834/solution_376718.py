def media_matriz(matriz):
    numeros = ()
    for A in matriz:
        for B in A:
        	numeros = numeros + (B,)
    media = round(sum(numeros)/len(numeros), 2)
    return media