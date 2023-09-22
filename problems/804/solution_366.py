def filtra_pares (a, b, c, d):
	'''funcao que filtra uma tupla com quatro elementos e retorna uma nova tupla de apenas elementos pares da tupla otiginal
    	tupla -> tupla'''
	if (a%2, b%2, c%2, d%2) == (0, 0 ,0 , 0):
        return (a, b, c, d)
    elif (a%2, b%2, c%2, d%2) == (0, 0, 0, 1):
        return (a, b, c)
    elif (a%2, b%2, c%2, d%2) == (0, 0, 1, 0):
        return (a, b, d)
    elif (a%2, b%2, c%2, d%2) == (0, 1, 0, 0):
        return (a, c, d)
    elif (a%2, b%2, c%2, d%2) == (1, 0, 0, 0):
        return (b, c, d)