def  bolos(A, B, C):
	""" Esta funcao calcula a quantidade de bolos que da para fazer, dado a quantidade de ingredientes"""
    return min(A//2, B//3, C//5)