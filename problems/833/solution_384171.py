def conta_numero(numero,matriz):
    """
    
"""
    soma=0
    sequencia=0
    for sequencia in range(len(matriz)):
        contador=matriz[sequencia].count(numero)
        soma+=contador
	return soma