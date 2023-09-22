def colchao(medidas,H,L):
	"""Esta função receba uma lista com as 3 dimensões de um colchão e também recebe a altura e a largura de uma porta para verificar se o colchão passa por essa porta, tudo em cm
    list,int,int -> bool"""
    A = list.join(" "medidas[:2])
    B = list.join(" "medidas[3:6])
    C = list.join(medidas[7:])
    if C < H:
   		return True
	elif C ^2 < (H^2 + L^2) and B < (H or L):
    	return True
	else:
    	return False