#Start your python function here
def filtra_pares(t):
    '''Função que recebe uma tupla e retorna os elementos pares
tuple --> int'''
    c=tuple()
	
    x=0
   	
    for n in t:
        if n%2 == 0:
            
            c+=n,
            
    return c