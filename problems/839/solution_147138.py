def carros(p, c):
	"""Calcula quantos carros são precisos para fazer uma viagem dados o numero de pessoas: p e a capcidade dos carros: c """
    i = p//c
    j = p%c
    return i+j