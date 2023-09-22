def colchao(medidas,H,L):
	"""Esta função receba uma lista com as 3 dimensões de um colchão e também recebe a altura e a largura de uma porta para verificar se o colchão passa por essa porta, tudo em cm
    list,int,int -> bool"""
    A = int(medidas[7:10])
    if A < H:
   		return True
	elif A ^2 < (H^2 + L^2):
    	return True
	else:
    	return False