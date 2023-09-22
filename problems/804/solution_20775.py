def filtra_pares(a):
    '''filtra os numeros pares e retorna uma tupla contendo os mesmos ordenadamente'''
    '''tup(int,int,int,int)->tup(int,int,int,int)'''
    filtro = ()
    if a[0]%2==0:
        filtro = filtro + (a[0],)
    if a[1]%2==0:
        filtro = filtro + (a[1],)
    if a[2]%2==0:
        filtro = filtro + (a[2],)
    if a[3]%2==0:
        filtro = filtro + (a[3],)
    return filtro