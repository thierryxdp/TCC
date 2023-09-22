def filtra_pares(tupla):
    '''
    função que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    a = []
    if tupla[0]%2 == 0:
        a = a + [tupla[0]]
        return a
    if tupla[1]%2 == 0:
        a = a + [tupla[1]]
        return a
    if tupla[2]%2 == 0:
        a = a + [tupla[2]]
        return a + [tupla[2]]
    if tupla[3]%2 == 0:
        a = a + [tupla[3]]
        return a