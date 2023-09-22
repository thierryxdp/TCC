def qtd_divisores(n):
    """Retorna a quantidade de divisores de um numero.int-->int"""
    divisores=0
    for numero in range(n):
        if numero!=0:
            if n%numero==0:
            	divisores=divisores+1
        	if n%numero!=0:
            	divisores=divisores
        if numero==0:
            divisores=divisores
    return divisores