def numero_par (x):
    if (x % 2 == 0):
    	return True
    else:
        return False
    

def filtra_pares (s):
    return tuple(filter(numero_par,s))#Start your python function here