def qtd_divisores(n):
    """Recebe um número e retorna a quantidade de divisores desse número;
    int -> int"""
    divisores = []
    for numero in range(1, n+1):
        if n%numero == 0:
            divisores.append(numero)
    return len(divisores)

def primo(n):
    """Recebe um número e verifica se ele é primo ou não;
    int -> bool"""
	if qtd_divisores(n) <= 2 and qtd_divisores(n) > 0:
        return True
    else:
        return False