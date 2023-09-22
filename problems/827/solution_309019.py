def qtd_divisores(numero):
	'''Esta função verifica quantos divisores têm um
	número
	int -> int'''
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1
            
    return qtd