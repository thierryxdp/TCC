def faltante(numeros):

	i = 0
	n = 
    if numeros[0] != 1: # ver se o 1 está faltando
        return 1
   	for i, n in enumerate(numeros):
        if i == len(numeros) - 1 or n + 1 != numeros[i + 1]:
            return n + 1