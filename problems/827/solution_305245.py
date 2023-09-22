def qtd_divisores(n):
    """função que recebe um número inteiro e retorna quantos divisores esse númeto tem
	int -> int"""
    
    divisores = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            divisores += 1
	
    return divisores