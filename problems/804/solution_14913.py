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
    
    if (not(tupla[0]%2 == 0)) and (not(tupla[1]%2 == 0)) and (not(tupla[2]%2 == 0)) and (not(tupla[3]%2 == 0)):
        return ()
    
    if (tupla[0]%2 == 0) and (tupla[1]%2 == 0) and (tupla[2]%2 == 0):
        return tupla[0] + tupla[1] + tupla [2]
    
    if (tupla[0]%2 == 0) and (tupla[1]%2 == 0) and (tupla[3]%2 == 0):
        return tupla[0] + tupla[1] + tupla [3]
    
    if (tupla[0]%2 == 0) and (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tupla[0] + tupla[2] + tupla [3]
    
    if (tupla[1]%2 == 0) and (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tupla[1] + tupla[2] + tupla [3]
    
    if (tupla[0]%2 == 0) and (tupla[1]%2 == 0):
        return tupla[0] + tupla[1]
    
    if (tupla[0]%2 == 0) and (tupla[2]%2 == 0):
        return tupla[0] + tupla[2]
    
    if (tupla[0]%2 == 0) and (tupla[3]%2 == 0):
        return tupla[0] + tupla[3]
    
    if (tupla[1]%2 == 0) and (tupla[2]%2 == 0):
        return tupla[1] + tupla[2]
    
    if (tupla[1]%2 == 0) and (tupla[3]%2 == 0):
        return tupla[1] + tupla[3]
    
    if (tupla[2]%2 == 0) and (tupla[3]%2 == 0):
        return tupla[2] + tupla[3]