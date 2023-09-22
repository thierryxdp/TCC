#Start your python function here
def filtra_pares(numeros):
    [n1,n2,n3,n4] = numeros
    par = ()
    
    if n1 % 2 == 0:
    	par = (*par, n1)
    if n2 % 2 == 0:
        par = (*par, n2)
    if n3 % 2 == 0:
        par = (*par, n3)
    if n4 % 2 == 0:
        par = (*par, n4)
	
    return par