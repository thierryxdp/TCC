def filtra_pares (t):
    """Função que filtra uma tupla deixando apenas os pares
	Recebe uma tupla de 4 numeros
	Retorna apenas os numeros pares"""
    lista = [] 
    if t[0] % 2 != 0:
        lista.append(t)
    	return tuple(lista)