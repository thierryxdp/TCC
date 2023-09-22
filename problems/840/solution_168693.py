def bolos(a,b,c):
	"""Função que define a quantidade de ingredientes necessários para retornar a quantidade de bolos possiveis de se fazer com os ingredientes dados"""
	return min((a//2),(b//3),(c//5))