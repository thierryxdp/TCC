def filtra_pares(tup):
    '''
    	Funçao que recebe uma tupla de inteiros e retorna os pares
    '''    
    if tup[0]%2 == 0 and tup[1]%2 == 0 and tup[2]%2 == 0 and tup[3]%2 == 0:
        return tup

    elif tup[0]%2 != 0 and tup[1]%2 == 0 and tup[2]%2 == 0 and tup[3]%2 == 0:
        return tup[1:3]

    elif tup[0]%2 == 0 and tup[1]%2 != 0 and tup[2]%2 == 0 and tup[3]%2 == 0:
        return tup[0] + tup[2:3]

    elif tup[0]%2 == 0 and tup[1]%2 == 0 and tup[2]%2 != 0 and tup[3]%2 == 0:
        return tup[0:1] + tup[3]

    else:
        return tup[0:2]