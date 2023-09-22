def bolos(A,B,C):
	'''Calcula a quantidade máxima de bolos que João
	consegue fazer, dados a quantidade de xícaras de farinha (A),
	de ovos (B) e de colheres de sopa de leite (C).'''
	return min(A//2,B//3,C//5)