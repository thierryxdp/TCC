def colchao(medidas,H,L):
	'''Função que calcula se um colchão tem a possibilidade de passar ou não em uma porta
	considerando a altura da porta H, largula L e as medidas do colchão em centímetros.
	Entrada: tupla
	Saída: bool'''
	if medidas[1]<=H:
		return True
	else: 
		return False