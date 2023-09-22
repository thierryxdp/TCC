def par(numero):
    '''Funcao booleana que retorna true quando passamos um numero par.
        Parametro de Entrada: int
        Valor de retorno: bool'''
    return numero%2 == 0

def filtra_pares(elem1,elem2,elem3,elem4):
    '''funcao que determina quais elementos sao pares e retorna apenas os pares em uma tupla
    entrada: int,int,int,int; saida: tupla'''
    if par(elem1) and par(elem2) and par(elem3) and par(elem4):
    	return (elem1,elem2,elem3,elem4)
    elif par(elem1) and par(elem2) and par(elem3):
        return (elem1, elem2, elem3)
    else:
        if par(elem1) and par(elem2) and par(elem4):
        	return (elem1,elem2,elem4)
        elif par(elem1) and par(elem3) and par(elem4):
            return (elem1, elem3, elem4)
        else:
            if par(elem2) and par(elem3) and par(elem4):
                return (elem2, elem3, elem4)
            elif par(elem1) and par(elem2):
            	return(elem1, elem2)
            else:
                if par(elem1) and par(elem3):
                    return(elem1, elem3) 
                elif par(elem1) and par(elem4):
                    return(elem1, elem4) 
                else:
                    if par(elem2) and par(elem3):
                    	return(elem2, elem3)
                    elif par(elem2) and par(elem4):
                    	return(elem2, elem4)
                    else:
                        if par(elem3) and par(elem4):
                    		return(elem3, elem4) 
                        elif par(elem1):
                            return (elem1,)
                        else:
                            if par(elem2):
                            	return (elem2,)
                            elif par(elem3):
                            	return (elem3,)
                            else:
                                if par(elem4):
                            		return (elem4,)
                                else:
                                    return (,)