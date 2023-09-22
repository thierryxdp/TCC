def primo (n):
    ''' 
    Retorna se o numero é primo
    ou não.
    int -> bool
    '''
    divisiveis = 0
    for valores in range(2,n):
        if (n%valores == 0):
            divisiveis = divisiveis + 1
            
    if (divisiveis == 0):
    	return False
    else:
    	return True