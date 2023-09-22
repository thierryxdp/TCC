import math
def bolos(A:int,B:int,C:int)->int:
	"""essa função retorna o maior número de bolos
	que podem ser feitos """
    return math.lcm(int(A//2),int(B//3),int(C//5))