def filtra_pares(n):
    '''funcao que recebe uma tupla com 4 valores inteiros "n" e retorna
    os valores pares na ordem informada da entrada'''
    pares = ()
    
    if (n[0])%2==0:
        pares=pares + (n[0],)
    if (n[1])%2==0:
        pares=pares + (n[1],)
    if (n[2])%2==0:
        pares=pares + (n[2],)
    if (n[3])%2==0:
        pares=pares + (n[3],)
        
    
    return pares