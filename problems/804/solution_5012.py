def par(n):
    if n % 2 == 0;
    	return True
    else:
        return False
def filtra_pares(b):
    return tuple(filter(par, b))