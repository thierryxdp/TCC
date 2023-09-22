def qtd_divisores(numero):
	"""conta quantos divisores um número tem
       int --> int"""
    j = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            j += 1
    return j