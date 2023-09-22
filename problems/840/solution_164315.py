def bolos(A, B, C):
    """A - 2 xícaras de farinha,
    B - 3 ovos,
    C - 5 colheres de leite"""
	farinha = A // 2
	ovos = B // 3
	leite = C // 5
	return min(farinha, ovos, leite)