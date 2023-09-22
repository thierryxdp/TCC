def qtd_divisores(n):
	'''conta a quantidade de divisores de n
    int -> int'''
    divisores = 0
    for i in range(n):
        if i % n == 0:
            divisores += 1
    return divisores