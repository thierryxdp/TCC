def filtra_pares (t):
    """Função que filtra uma tupla deixando apenas os pares
	Recebe uma tupla de 4 numeros
	Retorna apenas os numeros pares"""
    listaf = [] 
	for n in t:
        if n % 2 == 0:
            listaf.append(n)
    return tuple(listaf)