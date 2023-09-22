#Start your python function here
def filtra_pares(tupla):
    """ Recebe uma tupl como 4 nnum inteiros e retorna uma nova tupla contendo apenas os elementos pares.
    	Os valores de entrada são do tipo tupla(num1, nnum2, num3 num4) e retornam uma tupla. """
	if((tupla[0] % 2) == 0 ):
            if(tupla[1] % 2 == 0):
                if(tupla[2] % 2 == 0):
                    if(tupla[3] % 2 == 0):
                        return tupla[0],tupla[1],tupla[2], tupla[3] 
                    else:
                        return tupla[0],tupla[1],tupla[2]
                else:
            if(tupla[3] % 2 == 0):
                return tupla[0],tupla[1], tupla[3] 
            else:
                return tupla[0],tupla[1]
        else:
            if(tupla[2] % 2 == 0):
                if(tupla[3] % 2 == 0):
                    return tupla[0], tupla[2], tupla[3]
                else: 
                    return tupla[0], tupla[2]
            else:
                 if(tupla[3] % 2 == 0):
                 
                    return tupla[0], tupla[3]
				 else:
                    return tupla[0],
    else:
        if(tupla[1] % 2 == 0):
            if(tupla[2] % 2 == 0):
                if(tupla[3] % 2 == 0):
                    return tupla[1], tupla[2], tupla[3]
                else: 
                    return tupla[1],tupla[2]
            else:
                if(tupla[3] % 2 == 0):
                    return tupla[1], tupla[3]
                else:
                    return tupla[1]
                    
        else:
    		if(tupla[2] % 2 == 0):
                    if(tupla[3] % 2 == 0):
                        return tupla[2], tupla[3]
                    else: 
                        return tupla[2],
                else:
                    return "()"