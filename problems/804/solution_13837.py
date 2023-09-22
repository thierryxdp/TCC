def par(n):
    '''n inteiro'''
    return (n%2)==0
def impar(n):
    return not par(n)
def filtra_pares(t):
    ''' Recebe uma tupla com quatro elementos e retorna
    uma nova tupla contendo os elementos pares'''
    #casos de teste:
    '''filtra_pares((1,2,3,4)) -> (2,4)
       filtra_pares((10,23,44,50)) -> (10,44,50)
       filtra_pares((100,500,23,6)) -> (100,500,6)'''
    a = ()
    if par(t[0]):
         a = a + (t[0],)
    if par(t[1]):
        a = a + (t[1],)
    if par (t[2]):
        a = a + (t[2],)
    if par(t[3]):
        a = a + (t[3],)
    return a