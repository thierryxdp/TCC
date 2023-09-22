def primo(numero):
    """verifica se um numero e primo ou nao. int -> bool"""
    i=2
    while i in range(numero):
        if numero%i == 0:
            i += 1
    		return 	False
        else:
            i += 1
	return True