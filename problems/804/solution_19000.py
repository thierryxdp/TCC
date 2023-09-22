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

    nt = t in y

    
    
    if t in y[0] :
        return y[0]
    else:
        return ()