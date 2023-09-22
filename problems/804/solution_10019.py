def filtra_pares(x):
    """ recebe uma tupla com quatro elementos e retorn uma nova tupla apenas com os elementos pares da tupla original;
    tupla->tupla """
   
    if(x[0]%2==0) and (x[1]%2==0) and (x[2]%2==0) and (x[3]%2==0):
        return x[0],x[1],x[2],x[3]
    elif (x[0]%2!=0) and (x[1]%2==0) and (x[2]%2==0) and (x[3]%2==0):
        return x[1],x[2],x[3]