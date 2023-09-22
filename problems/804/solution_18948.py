def filtra_pares(t):
    '''Função para determinar os elementos pares'''
    't = tupla4ele'
    'nt = novatupla'
    tupla4ele = ()
    
    tupla4ele = (t[0],t[1],t[2],t[3])

    y = t[0],t[1],t[2],t[3]%2==0

    x = t[0],t[1],t[2],t[3]%2!=0
    
    nt = list(y)

    if t[0] in y:
        return nt
    elif t[1] in y:
        return nt
    elif t[2] in y:
        return nt
    elif t[3] in y:
        return nt
    else:
        ()