def primo(n):
    """Retorna se um numero e primo ou nao.int-->bool"""
    divisores=0
    for numero in range(n+1):
        if numero!=0:
            if n%numero==0:
            	divisores=divisores+1
        	if n%numero!=0:
            	divisores=divisores
        if numero==0:
            divisores=divisores
    return divisores==2