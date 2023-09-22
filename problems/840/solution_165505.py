import math
def bolos(A:int,B:int,C:int)->int:
	"""essa função retorna o maior número de bolos
	que podem ser feitos """
    #testando no IDLE funciona com 3 argumentos
	return math.gcd(C//5,(math.gcd A//2,B//3))