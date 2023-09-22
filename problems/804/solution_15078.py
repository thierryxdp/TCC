def filtra_pares(x):
    '''
    	Função que recebe uma tupla com 4 elementos e retorna uma nova tupla com apenas os elementos pares da tupla de entrada
        tupla -> tupla
    '''
    if x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0:
        return (x[0],x[1],x[2],x[3])
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0:
        return (x[1],x[2],x[3])
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2==0:
        return (x[0],x[2],x[3])
    elif x[0]%2==0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2==0:
        return (x[0],x[1],x[3])
    elif x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        return (x[0],x[1],x[2])
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2==0:
        return (x[2],x[3])
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2==0:
        return (x[1],x[3])
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        return (x[1],x[2])
    elif x[0]%2==0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        return (x[0],x[1])
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0:
        return (x[0],x[3])
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0:
        return (x[0],x[2])
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0:
        return (x[3])
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0:
        return (x[2])
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        return (x[1])
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        return (x[0])
    else:
        return ()