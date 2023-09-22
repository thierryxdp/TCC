def filtra_pares(tupl):
    '''Retorna uma tupla apenas com os numeros pares 
    da tupla original, na mesma ordem em que estavam;
    tupla (int,int,int,int) -> tupla'''
    if (tupl[0]%2)==0 and (tupl[1]%2)==0  and (tupl[2]%2)==0  and (tupl[3]%2)==0:
        return tupl[0:]
    elif (tupl[0]%2)!=0 and (tupl[1]%2)==0  and (tupl[2]%2)==0  and (tupl[3]%2)==0:
        return tupl[1:]
    elif (tupl[0]%2)!=0 and (tupl[1]%2)!=0  and (tupl[2]%2)==0  and (tupl[3]%2)==0:
        return tupl[2:]
    elif (tupl[0]%2)!=0 and (tupl[1]%2)!=0  and (tupl[2]%2)!=0  and (tupl[3]%2)==0:
        return tupl[3:]
    elif (tupl[0]%2)!=0 and (tupl[1]%2)!=0  and (tupl[2]%2)!=0  and (tupl[3]%2)!=0:
        return tupl[]