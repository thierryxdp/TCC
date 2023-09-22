""" Cálculo das dimensões máximas de um colchão para que passe
na porta """
def colchao(medidas,H,L):
    if medidas[1] <= L:
		return True
    if medidas[1] <= H :
        return True
    if medidas[2] <=L:
        return True
    if medidas[2] <=H:
        return True
    else:
        return False