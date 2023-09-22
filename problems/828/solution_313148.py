def primo(n):
    """A funcao verifica se o numero e primo ou nao; int->bool"""
	i=int(n/2)
    resultado = True
    while i>1:
        if n%i == 0:
        	resultado = False
        i=i-1
    return resultado