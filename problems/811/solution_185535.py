""" Cálculo das dimensões máximas de um colchão para que passe
na porta """
def colchao(medidas,H,L):
    if medidas[1] or medidas[2] <= H:
    	return True
    if medidas[1] or medidas[2] <= L:
        return True