def filtra_pares(tupla):
    '''
    função que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    tupl = tuple(tupla)
    a = ()
    if tupl[0]%2 == 0:
        b = (tupla[0])
    if tupl[0]%2 == 1:
        b = ()
    if tupl[1]%2 == 0:
        c = (tupla[1])
    if tupl[1]%2 == 1:
        c = ()
    if tupl[2]%2 == 0:
        d = (tupla[2])
    if tupl[2]%2 == 1:
        d = ()
    if tupl[3]%2 == 0:
        e = (tupla[3])
    if tupl[3]%2 == 1:
        e = ()
        return a+b+c+d+e