def filtra_pares(t):
    '''Função para determinar os elementos pares'''

    tupla1 = (t)
    
    y = t[0],t[1],t[2],t[3]%2==0
    if y == t:
        return tupla1
    else:
        return ()