bolos(A:int,B:int,C:int)->int:
	"""essa função retorna o maior número de bolos
	que podem ser feitos """
	return(math.gcd(A/2,B/3,C/5)