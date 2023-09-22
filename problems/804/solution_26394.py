def par(y):
    return x%2 ==0
    '''assinatura: int,int,int,int > int,int,int,int
    casos de teste: filtra_pares([2,3,4,5]) ==(2, 4)
    filtra_pares([24,10,-3,7]) ==(24, 10)
    filtra_pares([4,4,4,4]) ==(4, 4, 4, 4)'''
def filtra_pares(x):
    p = ()
    if par(x[0]):
        p = p + (x[0],)
    if par(x[1]):
        p = p + (x[1],)
    if par(x[2]):
        p = p + (x[2],)
    if par(x[3]):
        p = p + (x[3],)
    return p