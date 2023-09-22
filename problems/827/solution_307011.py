def qtd_divisores(numero):
    """recebe um numero e retorna o numero de sivisores que esse numero possui
    int -> int"""
    
    d = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            d += 1
    
	return d