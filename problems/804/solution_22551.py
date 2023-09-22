#Start your python function here
def filtra_pares(tupla_pares):
    pares = ()
    if tupla_pares[0] %2 == 0:
    	pares += (tupla_pares[0],)
        
    if tupla_pares[1] %2 == 0:
        pares += (tupla_pares[1],)
        
    if tupla_pares[2] %2 == 0:
        pares += (tupla_pares[2],)
        
    if tupla_pares[3] %2 == 0:
        pares += (tupla_pares[3],)
        
    return pares