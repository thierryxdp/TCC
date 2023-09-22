#Start your python function here
def filtra_pares(tup):
    ''' verifica se cada elemento é par e os inclui numa tuple. Ao fim retorna a lista
    	tup(int,int,int,int)--> tup(int,int,int,int)''' 
    pares = ()
    if(tup[0]%2 == 0):
        pares = pares + (tup[0],)
    if(tup[1]%2 == 0):
        pares = pares + (tup[1],)    
    if(tup[2]%2 == 0):
        pares = pares + (tup[2],)    
    if(tup[3]%2 == 0):
        pares = pares + (tup[3],)
        
    return pares