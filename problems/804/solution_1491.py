def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    for x, y, z, d in tupla:
        if x%2==0:
            return x
        elif y%2==0:
            return y
        elif z%2==0:
            return z
        elif d%2==0:
            return d