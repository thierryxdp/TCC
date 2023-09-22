def melhor_volta(matriz):
    numeros = []
    for A in matriz:
        for B in A:
        	numeros = numeros + [B]
    list.sort(numeros)
    maisrapido = numeros[0]
    return maisrapido