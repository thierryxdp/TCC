def filtra_pares(info):
    '''Filtra os pares de uma tupla com 4 elementos inteiros, devolvendo outra tupla apenas
	com os valores pares em suas respectivas posições'''
    if (info[0])% == 0:
        if info[1]% == 0:
            if info[2]% == 0:
            	if info[3]% == 0:
        			return info[0],info[1],info[2],info[3]
                else:
                    return info[0],info[1],info[2]
            else:
                if info[3]% == 0:
        			return info[0],info[1],info[3]
                else:
                    return info[0],info[1]
    	else:
            if info[2]% == 0:
            	if info[3]% == 0:
        			return info[0],info[2],info[3]
                else:
                    return info[0],info[2]
            else:
                if info[3]% == 0:
        			return info[0],info[3]
                else:
                    return info[0],
 	else:
        if info[1]% == 0:
            if info[2]% == 0:
            	if info[3]% == 0:
        			return info[1],info[2],info[3]
                else:
                    return info[1],info[2]
            else:
                if info[3]% == 0:
        			return info[1],info[3]
                else:
                    return info[1]
    	else:
            if info[2]% == 0:
            	if info[3]% == 0:
        			return info[2],info[3]
                else:
                    return info[2],
            else:
                if info[3]% == 0:
        			return info[3],
                else:
                    return (,)