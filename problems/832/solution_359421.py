def eh_quadrada(matrz):
    '''retorna se uma matrz é quadrada ou não
    [[]] -> true/false'''
    
    nCol = len(matrz)
    if(nCol == 0):
        return True
    nLin = len(matrz[0])
	  
    if (nCol == nLin):
    	return True
    else:
		return False