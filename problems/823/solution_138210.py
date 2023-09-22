def faltante(numeros):

	i = 0
	n = -1
    if numeros[0] != 1: # ver se o 1 está faltando
        return 1
    while i == len(numeros) - 1 or n + 1 != numeros [i + 1]:
			return n + 1