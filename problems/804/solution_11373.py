def filtra_pares(a,b,c,d):
    '''recebe uma tupla com 4 números inteiros e retorna
    apenas aqueles que são pares
    tupla -> tupla'''
    
    tup_vazia = ()
    
    if a % 2 == 0:
    tup_vazia += (a,)
    
    if b % 2 == 0: 
    tup_vazia +=  (b,)
    
    if c % 2 == 0:
    tup_vazia +=  (c,)
    
    if d % 2 == 0:
    tup_vazia +=  (d,)
    
    return tup_vazia()