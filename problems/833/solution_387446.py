def conta_numero(numero,matriz):
    """Função que dada um número e uma matriz, retorna quantas vezes esse número aparece na matriz."""
    """int,list--->int"""
    resposta=0
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
        	if matriz[l][c]==numero:
    resposta+=1
 	return resposta