def melhor_volta(matriz):
    numeros = []
    contador = 0
    volta = 0
    for A in matriz:
        for B in A:
        	numeros = numeros + [B]
    list.sort(numeros)
    melhortempovolta = numeros[0]
	while melhortempovolta not in matriz[contador]:
        volta = volta + 1
        contador = contador + 1
    volta = volta + 1
    @qualvolta = list.index(matriz[volta], melhortempovolta)
    return (volta, melhortempovolta)