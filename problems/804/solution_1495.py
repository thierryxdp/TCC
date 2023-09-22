def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    for x in tupla:
    for y in tupla:
    for z in tupla:
    for d in tupla:
        if x%2==0 and y%2==0 and z%2==0 and d%2==0:
            return x,y,z,d
        elif x%2=-0 and y%2==0 and z%2==0 and d%2==0:
            return y,z,d
        elif x%2=-0 and y%2=-0 and z%2==0 and d%2==0:
            return z,d
        elif x%2=-0 and y%2=-0 and z%2=-0 and d%2==0:
            return d