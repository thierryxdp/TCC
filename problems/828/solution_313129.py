def primo(n):
    """A funcao verifica se o numero e primo ou nao; int->bool"""
	i=n/2
    resultado = False
    while i>1:
        if n%i != 0:
        	resultado = True
        i=i-1
        return resultado