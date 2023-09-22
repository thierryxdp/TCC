def colchao(medidas,H,L):
	"""Função que, dadas as dimensões da porta e do colchão,
    retorna se o colchão passará pela porta ou não."""
    if medidas[1]<=H or medidas[1]<=L:
        return True
    if medidas[1]>H or medidas[1]>L:
        return False