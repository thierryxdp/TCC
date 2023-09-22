#Start your python function here
def filtra_pares(t):
    if (t[0]% 2) ==0:
        
    	return t[0:] + filtra_pares(t)