def filtra_pares(tupla):
    '''
    função que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    a = []
    if tupla[0]%2 == True:
        b = [tupla[0]]
    if tupla[0]%2 == False:
        b = []
        return a+b
    if tupla[1]%2 == True:
        c = [tupla[1]]
    if tupla[1]%2 == False:
        c = []
        return a+b+c
    if tupla[2]%2 == True:
        d = [tupla[2]]
    if tupla[2]%2 == False:
        d = []
        return a+b+c+d
    if tupla[3]%2 == True:
        e = [tupla[3]]
    if tupla[3]%2 == False:
        e = []
        return a+b+c+d+e