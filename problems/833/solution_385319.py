def conta_numero(numero, matriz):
    """função que dado um número inteiro e uma matriz(inteiros), conta e retorna quantas vezes o numero aparece na matriz
	int, list -> int"""
    
    quant = 0
    
    for lin in matriz:
        quant = quant + list.count(lin, numero)
    return quant