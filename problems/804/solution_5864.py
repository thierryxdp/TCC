def filtra_pares(a):
    '''Função que recebe uma tupla a contendo 4 números inteiros
    (int1,int2,int3,int4) e retorna uma nova tupla apenas com os
    elementos pares da original. tuple->tuple'''
    x=()
    if a[0]%2==0:
     x = x+(a[0],)
    if a[1]%2==0:
     x=x+(a[1],)
    if a[2]%2==0:
     x=x+(a[2],)
    if a[3]%2==0:
     x=x+(a[3],)
    return x