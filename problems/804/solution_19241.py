def par(numero):
    '''Funcao booleana que retorna true quando passamos um numero par.
        Parametro de Entrada: int
        Valor de retorno: bool'''
    return numero%2 == 0

def filtra_pares(tupla):
    '''funcao que determina quais elementos sao pares e retorna apenas os pares em uma tupla
    entrada: tupla; saida: tupla''' 
    if par((tupla)[0]) and par((tupla)[1]) and par((tupla)[2]) and par((tupla)[3]):
    	return ((tupla)[0],(tupla)[1],tupla)[2],tupla)[3])
    elif par((tupla)[0]) and par((tupla)[1]) and par((tupla)[2]):
        return ((tupla)[0], (tupla)[1], (tupla)[2])
    else:
        if par((tupla)[0]) and par((tupla)[1]) and par((tupla)[3]):
        	return ((tupla)[0],(tupla)[1],(tupla)[3])
        elif par((tupla)[0]) and par((tupla)[2]) and par((tupla)[3]):
            return ((tupla)[0], (tupla)[2], (tupla)[3])
        else:
            if par((tupla)[1]) and par((tupla)[2]) and par((tupla)[3]):
                return ((tupla)[1], (tupla)[2], (tupla)[3])
            elif par((tupla)[0]) and par((tupla)[1]):
            	return((tupla)[0], (tupla)[1])
            else:
                if par((tupla)[0]) and par((tupla)[2]):
                    return((tupla)[0], (tupla)[2]) 
                elif par((tupla)[0]) and par((tupla)[3]):
                    return((tupla)[0], (tupla)[3]) 
                else:
                    if par((tupla)[1]) and par((tupla)[2]):
                    	return((tupla)[1], (tupla)[2])
                    elif par((tupla)[1]) and par((tupla)[3]):
                    	return((tupla)[1], (tupla)[3])
                    else:
                        if par((tupla)[2]) and par((tupla)[3]):
                    		return((tupla)[2],(tupla)[3]) 
                        elif par((tupla)[0]):
                            return ((tupla)[0],)
                        else:
                            if par((tupla)[1]):
                            	return ((tupla)[1],)
                            elif par((tupla)[2]):
                            	return ((tupla)[2],)
                            else:
                                if par((tupla)[3]):
                            		return ((tupla)[3],)
                                else:
                                    return ()