def primo(n):
    """dado um numero inteiro positivo, verifica se ele é primo ou não.
    int -> bool"""
    for i in range(2, floor(sqrt(n) + 1)):
        if n % i == 0:
            return True
	return False