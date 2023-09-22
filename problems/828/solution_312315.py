def primo(n):
    """Dado um número inteiro positivo, verifica se esse número é primo ou
    não, retorando True para primo e False caso contrário."""
    if n<=1:
        return False
    elif n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
	return True