def qtd_divisores(numero):
	"""conta quantos divisores um número tem
       int --> int"""
    j = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            j += 1
    return j

def primo(numero):
    """Verifica se o número é primo
       int --> boolean"""
    if qtd_divisores(numero) <= 2:
        return False
    else:
        return True