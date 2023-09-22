def conta_numero(numero, matriz):
    """Dado um numero e uma matriz, retorna a quantidade de aparicoes deste nela
entrada:
	numero, matriz -> int, list
saida: int"""
    
    vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == numero:
                vezes += 1
    return vezes