def colchao (medidas,H,L):
	"""verifica e retorna se o colchão de medidas [A,B,C]
    passa na porta de sua casa, de altura H e largura L
    list, float, float -> bool"""
    return (medidas[1]<=H)and(medidas[0]<=L)