def filtra_pares (t):
    """Função que filtra uma tupla deixando apenas os pares
	Recebe uma tupla de 4 numeros
	Retorna apenas os numeros pares"""
    listaf = [] 
    if int(t[0]) % 2 != 0:
        listaf.append(t)
    if t[1] % 2 != 0:
        listaf.append(t)
    if t[2] % 2 != 0:
        listaf.append(t)
    if t[3] % 2 != 0:
        listaf.append(t)
    return tuple(listaf)