def filtra_pares(tupla):
    '''
    funcao criada para retornar somente os elementos pares da tupla colocada, 
    na mesma ordem em que se encontravam
    parametros:
    tupla: quatro elementos inteiros
    saida:
    elementos pares da tupla
    '''
    a,b,c,d = tupla
    
    if a%2 == 0:
        a == True
    else:
        a = False
        
    if b%2 == 0:
        b == True
    else:
        b = False
        
    if c%2 == 0:
        c == True
    else:
        c = False
    
    if d%2 == 0:
        d == True
    else:
        d = False
    
    pares = filter(None,(a,b,c,d))
    
    return tuple(pares)