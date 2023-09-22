def filtra_pares(tupla):
    '''
    função que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    a = []
    if tupla[0]%2 == True:
        b = a + [tupla[0]]
        return b
    if tupla[1]%2 == True:
        c = b + [tupla[1]]
        return c
    if tupla[2]%2 == True:
        d = c + [tupla[2]]
        return d
    if tupla[3]%2 == True:
        e = d + [tupla[3]]
        return e