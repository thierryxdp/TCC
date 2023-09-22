def filtra_pares(truple):
    elemento1 = truple[0]%2
    elemento2 = truple[1]%2
    elemento3 = truple[2]%2
    elemento4 = truple[3]%2
    newTruple = []
    
    if elemento1 == 0:
        newTruple = [elemento1]
        if elemento2 == 0:
    		newTruple = [elemento1, elemento2]
			if elemento3 == 0:
            	newTruple = [elemento1, elemento2, elemento3]
            	if elemento4 == 0:
                	newTruple = [elemento1, elemento2, elemento3, elemento4]
    else:
    	if elemento2 == 0:
    		newTruple = [elemento2]
        	if elemento3 == 0:
            	newTruple = [elemento2, elemento3]
            		if elemento4 == 0:
                		newTruple = [elemento2, elemento3, elemento4]
        else:
            if elemento3 == 0:
            	newTruple = [elemento3]
            		if elemento4 == 0:
                		newTruple = [elemento3, elemento4]
            else:
                if elemento4 == 0:
                		newTruple = [elemento4]
	return newTruple