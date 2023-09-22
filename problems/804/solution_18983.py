def filtra_pares(t):
    '''Função para determinar os elementos pares'''
    't = tupla4ele'
    'nt = novatupla'
    tupla4ele = ()
    
    tupla4ele = (t[0],t[1],t[2],t[3])
    
    

    y = t[0],t[1],t[2],t[3]%2==0
    
    x = t[0],t[1],t[2],t[3]%2!=0

    nt = y[0], y[1], y[2], y[3]

    FP = t in y

    FP[0] = t == y[0]
    FP[1] = t == y[1]
    FP[2] = t == y[2]
    FP[3] = t == y[3]

    
    if t[0] == y[0] :
        return FP[0]
    else:
        return ()