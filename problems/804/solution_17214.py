def filtra_pares (tup):
    '''receba uma tupla com quatro elementos inteiros como
argumento, e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma
ordem em que se encontravam
:tuple --> tuple '''
    a = tup[0]
    b = tup[1]
    c = tup[2]
    d = tup[3]
    msg = 'os pares são '
    if ((a%2)==0):
        msg = msg  +  str(a) + ' e '
    if ((b%2)==0):
        msg = msg  +  str(b)+ ' e '
    if ((c%2)==0):
        msg = msg  +  str(c)+ ' e '
    if ((d%2)==0):
        msg = msg  +  str(d)
    return msge