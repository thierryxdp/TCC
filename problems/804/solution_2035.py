def filtra_pares(tup):
    '''Funcao recebe uma tupla tup com 4 elementos inteiros e retorna uma nova tupla 
contendo apenas os elementos pares da tupla tup.
	Parametros de entrada: tuple (int,int,int,int)
    Valor de retorno: tuple'''
	if tup[0]%2==0:
        elemento1=tup[0]
        if tup[1]%2==0:
            elemento2=tup[1]
            if tup[2]%2==0:
                elemento3=tup[2]
                if tup[3]%2==0:
                    elemento4=tup[3]
                    return (elemento1,elemento2,elemento3,elemento4)
                else:
                    return (elemento1,elemento2,elemento3)
            elif tup[3]%2==0:
                elemento3=tup[3]
                return (elemento1,elemento2,elemento3)
            else:
                return (elemento1, elemento2)
        elif tup[2]%2==0:
            elemento2=tup[2]
            if tup[3]%2==0:
                elemento3=tup[3]
                return (elemento1, elemento2,elemento3)
            else:
                return (elemento1, elemento2)
        elif tup[3]%2==0:
            elemento2=tup[3]
            return (elemento1, elemento2)
        else:
            return (elemento1)
    elif tup[1]%2==0:
        elemento1=tup[1]
        if tup[2]%2==0:
            elemento2=tup[2]
            if tup[3]%2==0:
                elemento3=tup[3]
                return (elemento1, elemento2,elemento3)
            else:
                return (elemento1, elemento2)
        elif tup[3]%2==0:
            elemento2=tup[3]
            return (elemento1, elemento2)
        else:
            return (elemento1)
    elif tup[2]%2==0:
        elemento1=tup[2]
        if tup[3]%2==0:
            elemento2=tup[3]
            return (elemento1, elemento2)
        else:
            return (elemento1)
    elif tup[3]%2==0:
        elemento1=tup[3]
        return (elemento1)
    else:
        return()