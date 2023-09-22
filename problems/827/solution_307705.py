def qtd_divisores(n):
    """função que recebe um número inteiro e retorna quantos divisores esse número possui
	int -> int"""
    
    divi = 0
    
    for i in range(1, n+1):
        if n%i == 0:
            divi = divi + 1
    
    return divi