def filtra_pares(tupla):
    '''
    	funcao que recebe como entrada uma tupla de quatro
        elementos inteiros e retorna uma nova tupla apenas
        com os elementos pares da primeira
        :param tupla: tuple
        : return: tuple
    '''
    if (tupla[0]%2 == 0) and (tupla[1]%2 == 0) and (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tupla
    
    elif (not(tupla[0]%2 == 0)) and (not(tupla[1]%2 == 0)) and (not(tupla[2]%2 == 0)) and (not(tupla[3]%2 == 0)):
        return ()
    
    elif (tupla[0]%2 == 0) and (tupla[1]%2 == 0) and (tupla[2]%2 == 0):
        return tuple((tupla[0], tupla[1], tupla [2]))
    
    elif (tupla[0]%2 == 0) and (tupla[1]%2 == 0) and (tupla[3]%2 == 0):
        return tuple((tupla[0], tupla[1], tupla [3]))
    
    elif (tupla[0]%2 == 0) and (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tuple((tupla[0], tupla[2], tupla [3]))
    
    elif (tupla[1]%2 == 0) and (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tuple((tupla[1], tupla[2], tupla [3]))
    
    elif (tupla[0]%2 == 0) and (tupla[1]%2 == 0):
        return tuple((tupla[0], tupla[1]))
    
    elif (tupla[0]%2 == 0) and (tupla[2]%2 == 0):
        return tuple((tupla[0], tupla[2]))
    
    elif (tupla[0]%2 == 0) and (tupla[3]%2 == 0):
        return tuple((tupla[0], tupla[3]))
    
    elif (tupla[1]%2 == 0) and (tupla[2]%2 == 0):
        return tuple((tupla[1], tupla[2]))
    
    elif (tupla[1]%2 == 0) and (tupla[3]%2 == 0):
        return tuple((tupla[1], tupla[3]))
    
    elif (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tuple((tupla[2], tupla[3]))
    
    elif (tupla[0]%2 == 0):
        return tuple((tupla[0]))
    
    elif (tupla[1]%2 == 0):
        return tuple((tupla[1]))
    
    elif (tupla[2]%2 == 0):
        return tuple((tupla[2]))
    
    else:
        return tuple((tupla[0]))