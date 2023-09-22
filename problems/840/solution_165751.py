def bolos(A,B,C):
	"""
	Função que recebe número de xícaras de farinha de trigo (A),
    número de ovos (B) e número de colheres de sopa de leite(C),
    e retorna a quantidade de bolos que João consegue fazer.
	"""
    bolosA=A//2
	bolosB=B//3
	bolosC=C//5
	if bolosA<=bolosB:
		if bolosA<=bolosC:
			return bolosA
	elif:
		if bolosB<=bolosC:
			return bolosB
	else:
		return bolosC