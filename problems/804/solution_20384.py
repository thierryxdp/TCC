def filtra_pares(t):
    '''
    	Funçao que recebe uma tupla de inteiros e retorna os pares
    '''    
	if t[:4]%2 == 0:
        return t
    elif t[:4]%2 != 0:
        return ()
    elif t[0]%2 != 0 and t[1:4]%2 == 0:
        return t[1:4]
    elif t[:1]%2 != 0 and t[2:4]%2 == 0:
        return t[2:4]
    elif t[:2]%2 != 0 and t[3:4]%2 == 0:
        return t[3:4]
    elif t[:3]%2 != 0 and t[4]%2 == 0:
        return t[4]
    elif t[0]%2 == 0 and t[1]%2 != 0 and t[2:4]%2 == 0:
        return t[0] + t[2:4]
    elif t[0]%2 == 0 and t[1:2]%2 != 0 and t[3:4]%2 == 0:
        return t[0] + t[3:4]
    elif t[0]%2 == 0 and t[1:3]%2 != 0 and t[4]%2 == 0:
        return t[0] + t[4]
    elif t[:1]%2 == 0 and t[2]%2 != 0 and t[3:4]%2 == 0:
        return t[:1] + t[3:4]
    elif t[:1]%2 == 0 and t[2:3]%2 != 0 and t[4]%2 == 0:
        return t[:1] + t[4]
    elif t[:1]%2 == 0 and t[2:4]%2 != 0:
        return t[:1]
    elif t[:2]%2 == 0 and t[3]%2 != 0 and t[4]%2 == 0:
        return t[:2] + t[4]
    elif t[:2]%2 == 0 and t[3:4]%2 != 0:
        return t[:2]
    else:
        return t[:3]