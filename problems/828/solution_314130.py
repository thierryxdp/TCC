import math
def qtd_divisores(numero):
    if numero < 0:
        return 0
    limite = math.(numero**(1/2))
    divisores = 0
    for i in range(1, limite+1):
        if numero % i == 0:
            divisores += 2
            
            if numero/i == i:
                divisores -= 1
    return divisores

def primo(n):
    divisores = qtd_divisores(n)
    if divisores == 2:
    	return True
	else:
        return False