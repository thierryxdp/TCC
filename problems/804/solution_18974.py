def filtra_pares(t):
    '''Função para determinar os elementos pares'''
    't = tupla4ele'
    'nt = novatupla'
    tupla4ele = ()
    
    tupla4ele = (t[0],t[1],t[2],t[3])
    
    

    y = t[0],t[1],t[2],t[3]%2==0
    
    x = t[0],t[1],t[2],t[3]%2!=0

    nt = y[0], y[1], y[2], y[3]

    if t[0] == y[0] and t[1] == x[x1]:
        return (t[0],)
    
    elif t[1] == y[1]:
        return(t[1],)
    
    elif t[0] == y[0] and t[1] == y[1]:
        return (t[0],t[1])
    elif t[0] == y[0] and t[1] == y[1] and t[2] == y[2]:
        return (t[0],t[1],y[2])
    elif t[0] == y[0] and t[1] == y[1] and t[2] == y[2] and t[3] == y[3]:
        return (t[0],t[1],t[2],t[3])
    else:
        return ()