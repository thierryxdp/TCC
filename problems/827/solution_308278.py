def qtd_divisores(N):
	"""recebe um numero e retorns a quantidade de divisores"""
	""" entrada: int saida: int"""
	divisores=0	
    for i in range(1, N+1):
        if N%i==0:
            divisores=divisores+1
        else:
            divisores=divisores+0
    return divisores