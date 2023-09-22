def conta_numero(numero,matriz):
    vezes = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(0,linha):
        for y in range(0,coluna):            
    		if numero in matriz[x][x]:
        		vezes += 1
    return vezes