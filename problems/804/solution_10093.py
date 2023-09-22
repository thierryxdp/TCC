def filtra_pares(x):
    '''Retorna uma tupla apenas com os numeros pares 
    da tupla original, na mesma ordem em que estavam;
    tupla (int,int,int,int) -> tupla'''
    if (x[0]%2)==0:
        a=x[0]
    elif (x[0]%2)!=0:
        a=()
    elif (x[1]%2)==0:
        b=x[1]
    elif (x[1]%2)!=0:
        b=()
    elif (x[2]%2)==0:
        c=x[2]
    elif (x[2]%2)!=0:
        c=()
    elif (x[3]%2)==0:
        d=x[3]
    elif (x[3]%2)!=0:
        d=()
    return x=(a,b,c,d)