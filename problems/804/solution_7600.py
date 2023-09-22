def filtra_pares(t):
    '''Recebe um tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas 
    os elementos pares da tupla original, na mesma ordem que se encontravam;
    tup -> tup'''
    if t[0]%2==0:
        w=t[0]
    if t[1]%2==0:
        x=t[1]
    if t[2]%2==0:
        y=t[2]
    if t[3]%2==0:
        z=t[3]
    return (w,x,y,z)