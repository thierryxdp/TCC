def filtra_pares(t):
    '''Função para determinar os elementos pares'''
    't = tupla4ele'
    'nt = novatupla'
    tupla4ele = ()
    
    tupla4ele = (t[0],t[1],t[2],t[3])
    
    

    y = t[0]%2==0,t[1]%2==0,t[2]%2==0,t[3]%2==0
    
    x = t[0],t[1],t[2],t[3]%2!=0
    
    nt= list(y)

    nt = y[0], y[1], y[2], y[3]
    ya = y[0]%2==0
    yb = y[1]%2==0
    yc = y[2]%2==0
    yd = y[3]%2==0
        
    if  y[0] == True :
        return t[0],
    elif y[1] == True:
        return t[1],
    elif y[2] == True:
        return t[2],
    elif y[3] == True:
        return t[3],
    
    elif y[0] and y[1] == True:
        return t[0], t[1]
    elif ya and yd == True:
        return t[0], + t[3]
    
    
    
    
    else:
        return ()