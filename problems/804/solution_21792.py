def filtra_pares(x):
    '''Funcao que filtra uma tupla de 4 elementos
    retornando apenas os pares e na mesma ordem.'''
    '''Entrada e uma tupla'''
    '''A saida sao os numeros pares na mesma ordem'''
	
    if x[0]%2==0:
        return (x[0],)
    elif x[1]%2==0:
        return (x[0], x[1])
    elif x[2]%2==0:
        return (x[0], x[1], x[2])
    elif x[3]%2==0:
        return (x[0], x[1], x[2], x[3])