def filtra_pares(t):
    ''' retorna uma tupla com elementos pares, dada uma tupla t com quatro elementos inteiros;
    int,int,int,int->tuple '''
    retorna=()
    if t[0]%2==0:
        retorna+=(t[0],)
    if t[1]%2==0:
        retorna+=(t[1],)
    if t[2]%2==0:
        retorna+=(t[2],)
    if t[3]%2==0:
        retorna+=(t[3],)
    return retorna