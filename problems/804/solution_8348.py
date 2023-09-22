def filtra_pares(t):
    '''Recebe uma tupla de 4 elementos como entrada e retorna uma nova tupla contendo
    apenas os elementos pares, na mesma ordem em que encontravam;
    tupla -> tupla'''
    if t[0]%2==0:
        a=t[0:1]
    if t[1]%2==0:
        b=t[1:2]
    if t[2]%2==0:
        c=t[2:3]
    if t[3]%2==0:
        d=t[3:]
    return a+b+c+d or a+b+c or a+b or a or b+c+d or b+c or b or c+d or c or d