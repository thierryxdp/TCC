def eh_quadrada(matrz):
    '''retorna se uma matrz é quadrada ou não
    [[]] -> true/false'''
    
    nCol = len(matrz)
    nLin = len(matrz[0])
  
    if (nCol == nLin or nCol == 0):
    	return True
    else:
		return False