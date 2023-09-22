""" Cálculo das dimensões máximas de um colchão para que passe
na porta """
def colchao(medidas,H,L):
    if medidas[1] <= (L or H):
		return True
    if medidas[1] > (L or H):
        return False