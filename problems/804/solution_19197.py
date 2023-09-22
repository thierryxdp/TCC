def filtra_pares(t):
    '''Retorna uma tupla que contem apenas os elementos pares
	Entrada: int,int,int,int
	Saída: tuple'''
    if t[0]%2!=0:
        return (t[1],t[2],t[3])
    elif t[1]%2!=0:
        return (t[0],t[2],t[3])
    elif t[2]%2!=0:    
        return (t[0],t[1],t[3])
    elif t[3]%2!=0:    
        return (t[0],t[1],t[2])