def filtra_pares (tuple):
	''' Filtragem de uma tupla com quatro números inteiros,
    onde no retorno os números pares ignorando os números
    impares '''
    tupla2 = tuple()
    
	if (t[0]%2)==0:
		tuple2 = tuple2 + (t[0],)
    if (t[1]%2)==0:
		tuple2 = tuple2 + (t[1],)
    if (t[2]%2)==0:
		tupla2 = tuple2 + (t[2],)
    if (t[3]%2)==0:
		tupla2 = tuple2 + (t[3],)
        return tuple2