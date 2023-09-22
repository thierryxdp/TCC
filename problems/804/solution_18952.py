def filtra_pares(t):
    '''Função para determinar os elementos pares'''
    't = tupla4ele'
    'nt = novatupla'
    tupla4ele = ()
    
    tupla4ele = (t[0],t[1],t[2],t[3])

    y = t[0],t[1],t[2],t[3]%2==0
    
    nt = list(y)
    
    
    x = t[0],t[1],t[2],t[3]%2!=0

    if t[0] in nt or t[1] in nt or t[2] in nt or t[3] in nt:
        return nt
    else:
        ()