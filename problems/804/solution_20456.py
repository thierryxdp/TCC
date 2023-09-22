def filtra_pares(tupla):
    '''
    função que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    a = []
    if tupla[0]%2 == True:
        return a + [tupla[0]]
    if tupla[1]%2 == True:
        return a + [tupla[1]]
    if tupla[2]%2 == True:
        return a + [tupla[2]]
    if tupla[3]%2 == True:
        return a + [tupla[3]]