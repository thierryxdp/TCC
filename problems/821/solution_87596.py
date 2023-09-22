def fatorial(n):
    """funcao que dado um número retorna o fatorial deste número
	int -> int"""
    
    num = n
    while n > 1:
        n = n - 1
        num = num * n 
        
	return num