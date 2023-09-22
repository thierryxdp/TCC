def par(numero):
    '''Funcao booleana que retorna true quando passamos um numero par.
        Parametro de Entrada: int
        Valor de retorno: bool'''
    return numero%2 == 0

def filtra_pares(tuple[elem1, elem2, elem3, elem4])
    '''funcao que determina quais elementos sao pares e retorna apenas os pares em uma tupla
    entrada: int,int,int,int; saida: tupla''' 
    tupla = [elem1, elem2, elem3, elem4]
    if par((tupla)[0]) and par((tupla)[1]) and par((tupla)[2]) and par((tupla)[3]):
    	return (tupla)
    elif par((tupla)[0]) and par((tupla)[1]) and par((tupla)[2]):
        return (elem1, elem2, elem3)
    else:
        if par((tupla)[0]) and par((tupla)[1]) and par((tupla)[3]):
        	return (elem1,elem2,elem4)
        elif par((tupla)[0]) and par((tupla)[2]) and par((tupla)[3]):
            return (elem1, elem3, elem4)
        else:
            if par((tupla)[1]) and par((tupla)[2]) and par((tupla)[3]):
                return (elem2, elem3, elem4)
            elif par((tupla)[0]) and par((tupla)[1]):
            	return(elem1, elem2)
            else:
                if par((tupla)[0]) and par((tupla)[2]):
                    return(elem1, elem3) 
                elif par((tupla)[0]) and par((tupla)[3]):
                    return(elem1, elem4) 
                else:
                    if par((tupla)[1]) and par((tupla)[2]):
                    	return(elem2, elem3)
                    elif par((tupla)[1]) and par((tupla)[3]):
                    	return(elem2, elem4)
                    else:
                        if par((tupla)[2]) and par((tupla)[3]):
                    		return(elem3, elem4) 
                        elif par((tupla)[0]):
                            return (elem1,)
                        else:
                            if par((tupla)[1]):
                            	return (elem2,)
                            elif par((tupla)[2]):
                            	return (elem3,)
                            else:
                                if par((tupla)[3]):
                            		return (elem4,)
                                else:
                                    return ()