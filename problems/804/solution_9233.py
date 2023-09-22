def filtra_pares (elementos):
    ''' (a, b, c, d)
    dada uma tupla com quatro elementos inteiros, calcula e retorna uma nova tupla contendo os elementos pares da tupla 
    original, na mesma ordem em que estavam.
       : int, int, int, int -> tuple 
    '''
    a = elementos[0]
    b = elementos[1]
    c = elementos[2]
    d = elementos[3]
    
    pares = ()
    if ((a%2)==0):
        pares = pares + (a)
    if ((b%2)==0):
        pares = pares + (b)
    if ((c%2)==0):
        pares = pares + (c)
    if ((d%2)==0):
        pares = pares + (d)
    return pares