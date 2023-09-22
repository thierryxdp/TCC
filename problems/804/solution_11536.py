def filtra_pares(x):
    """ recebe uma tupla com quatro elementos e retorn uma nova tupla apenas com os elementos pares da tupla original;
    tupla->tupla """
    pares=()
    
    if(x[0]%2==0):
        pares=pares + (x[0],)
    if(x[1]%2==0):
        pares=pares + (x[1],)
    if(x[2]%2==0):
        pares=pares + (x[2],)
    if(x[3]%2==0):
        pares=pares + (x[3],)
    return pares