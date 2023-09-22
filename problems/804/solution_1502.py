def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    for x in tupla:
        if x%2==0:
            return x
        for y in tupla:
            elif y%2==0 and y!=x:
                return y