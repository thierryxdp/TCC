def filtra_pares(tup):
    '''
    	Funçao que recebe uma tupla de inteiros e retorna os pares
    '''    
    if t[0]%2 == 0 and t[1]%2 == 0 and t[2]%2 == 0 and t[3]%2 == 0:
        return t

    elif t[0]%2 != 0 and t[1]%2 == 0 and t[2]%2 == 0 and t[3]%2 == 0:
        return t[1:3]

    elif t[0]%2 == 0 and t[1]%2 != 0 and t[2]%2 == 0 and t[3]%2 == 0:
        return t[0] + t[2:3]

    elif t[0]%2 == 0 and t[1]%2 == 0 and t[2]%2 != 0 and t[3]%2 == 0:
        return t[0:1] + t[3]

    else:
        return t[0:2]