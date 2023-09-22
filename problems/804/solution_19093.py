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
    
        
    if  y[0] == True :
        return t[0],
    elif y[1] == True:
        return t[1],
    elif y[2] == True:
        return t[2],
    elif y[3] == True:
        return t[3],
    
    elif y[0:1] == True:
        return t[0:1]
    elif y[0:2] == True:
        return t[0:2]
    elif y[0:3:1] == True:
        return t[0:3:1]
    elif y[0:3] == True:
        return t[0:3]

    elif y[0] and y[2] == True:
        return t[0], + t[2]
    elif y[0:3] == True:
        return t[0], + t[3]

    elif y[1:2] == True:
        return t[1:2]
    elif t[0] and t[3] == True:
        return t[1:3:1]
    else:
        return ()