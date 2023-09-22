def filtra_pares(a,b,c,d):
    '''
    retorna as tuplas pares
    int,int,int,int -> tuple
    '''
    param=()
    if(a%2=0):
        param=param + ('a' )
    elif (b%2=0):
        param=param + ('b' )
    elif (c%2=0):
        param=param + ('c' )
    elif (d%2=0):
        param=param + ('d' )
    else: param