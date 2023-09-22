def conta_numero(numero,matriz):
    """
"""
    soma=0
    num=0
    for num in range(len(matriz)):
        s=matriz[num].count(numero)
        soma+=s
	return soma