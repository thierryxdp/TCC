def colchao(medidas,H,L):
	"""Esta função receba uma lista com as 3 dimensões de um colchão e também recebe a altura e a largura de uma porta para verificar se o colchão passa por essa porta, tudo em cm
    list,int,int -> bool"""
    if medidas[7:] < H:
   		return True
	elif (medidas[7:])^2 < (H^2 + L^2):
    	return True
	else:
    	return False