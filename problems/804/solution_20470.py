def filtra_pares(t):
    '''
    	Funçao que recebe uma tupla de inteiros e retorna os pares
    '''       
	if t[0]%2 == 0 and t[1]%2 == 0 and t[2]%2 == 0 and t[3]%2 == 0:
        return t[0], t[1], t[2], t[3]
    elif  t[0]%2 != 0 and t[1]%2 != 0 and t[2]%2 != 0 and t[3]%2 != 0:
        return ''
    elif t[0]%2 != 0 and t[1]%2 == 0 and t[2]%2 == 0 and t[3]%2 == 0:
    	return t[1], t[2], t[3]
    elif t[0]%2 != 0 and t[1]%2 != 0 and t[2]%2 == 0 and t[3]%2 == 0:
        return t[2], t[3]
    elif t[0]%2 != 0 and t[1]%2 != 0 and t[2]%2 != 0 and t[3]%2 == 0:
        return t[3]
    elif t[0]%2 == 0 and t[1]%2 != 0 and t[2]%2 == 0 and t[3]%2 == 0:
        return t[0], t[2], t[3]
    elif t[0]%2 == 0 and t[1]%2 != 0 and t[2]%2 != 0 and t[3]%2 == 0:
        return t[0], t[3]