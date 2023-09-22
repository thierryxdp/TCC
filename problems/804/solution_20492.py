def filtra_pares(tupla):
    '''
    função que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    a = ()
    if tupla[0]%2 == 0:
        b = (tupla[0])
    if tupla[0]%2 == 1:
        b = ()
    if tupla[1]%2 == 0:
        c = (tupla[1])
    if tupla[1]%2 == 1:
        c = ()
    if tupla[2]%2 == 0:
        d = (tupla[2])
    if tupla[2]%2 == 1:
        d = ()
    if tupla[3]%2 == 0:
        e = (tupla[3])
    if tupla[3]%2 == 1:
        e = ()
        return tuple(a+b+c+d+e)