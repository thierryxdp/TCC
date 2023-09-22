def filtra_pares(t):
    '''Esta função recebe uma tupla de quatro números inteiros, 
      e retorna uma tupla nova com os números pares na tupla 
      recebida como entrada
      tup -> tup'''
    
    pares = ()
     
    if (t[0])%2==0:
        pares= pares + (t[0],) 
    if (t[1])%2==0:
        pares= pares + (t[1],)
    if (t[2])%2==0:
        pares= pares + (t[2],)
    if (t[3])%2==0:
        pares= pares + (t[3],)
        return pares
    elif (t[0])%2==0:
        pares= (t[0],)
        return pares 
    elif (t[1])%2==0:
        pares= (t[1],)
        return pares 
    elif (t[2])%2==0:
        pares= (t[2],)
        return pares 
    elif (t[3])%2==0:
        pares= (t[3],)
        return pares
    
    else:
        return ()