def filtra pares (n):
    '''recebe uma tupla com 4 valores inteiros n, entre pares e impares
    e retorna apenas os valores pares em ordem'''
    pares=()
    
    if (n[0])%2==0:
        pares=pares +(n[0],)
    if (n[1])%2==0:
        pares=pares +(n[1],)
    if (n[2])%2==0:
        pares=pares +(n[2],)
    if (n[3])%2==0:
        pares=pares +(n[3],)
    
    return pares