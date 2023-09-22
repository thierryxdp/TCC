def filtra_pares(tupl):
    '''Retorna uma tupla apenas com os numeros pares 
    da tupla original, na mesma ordem em que estavam;
    tupla (int,int,int,int) -> tupla'''
    if (tupl[0]%2)==0:
        a=tupl[0]
    elif (tupl[0]%2)!=0:
        a=()
    elif (tupl[1]%2)==0:
        b=tupl[1]
    elif (tupl[1]%2)!=0:
        b=()
    elif (tupl[2]%2)==0:
        c=tupl[2]
    elif (tupl[2]%2)!=0:
        c=()
    elif (tupl[3]%2)==0:
        d=tupl[3]
    elif (tupl[3]%2)!=0:
        d=()
    return tupl=(a,b,c,d)