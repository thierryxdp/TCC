def filtra_pares(tupla):
    '''dada quatro elementos de entrada, verifica os pares e os introdux a uma nova
    	tupla'''
    nv_tupla=()
    elif not(tupla[0]%2 ==0) or not(tupla[1]%2 ==0) and not(tupla[2]%2 ==0) and not(tupla[3]%2==0):
        return ()
    if tupla[0]%2 ==0:
        nv_tupla=nv_tupla +(tupla[0],)
    if tupla[1]%2 ==0:    
        nv_tupla=nv_tupla +(tupla[1],)
    if tupla[2]%2 ==0: 
        nv_tupla=nv_tupla +(tupla[2],)
    if tupla[3]%2 ==0:
        nv_tupla=nv_tupla +(tupla[3],)
    else:
        return nv_tupla
    if not(tupla[0]%2 ==0) or not(tupla[1]%2 ==0) and not(tupla[2]%2 ==0) and not(tupla[3]%2==0):
        return ()