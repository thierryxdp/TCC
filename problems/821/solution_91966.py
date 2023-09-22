def fatorial(x):
    '''calcula'''
    if x>1:
    	while x>1:
        	retorno = x*(x-1)
            x = x-1
        return retorno
    else:
        return 1