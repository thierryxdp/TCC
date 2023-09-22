#Start your python function here
def filtra_pares(t):
    filtra_pares = [] 
    if type(filtra_pares) == tuple and len(t) == 4:
    
         
        for i in t:
            if type(i) != int:
                filtra_pares = []
                return filtra_pares
                #break
            elif i%2 == 0:
                 lista.append(i)
        return(tuple(filtra_pares)) 
    else:
        return filtra_pares