def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    tupla=x,y,z,d
        if x%2==0 and y%2==0 and z%2==0 and d%2==0:
            return x,y,z,d
        elif x%2=-0 and y%2==0 and z%2==0 and d%2==0:
            return y,z,d
        elif x%2=-0 and y%2=-0 and z%2==0 and d%2==0:
            return z,d
        elif x%2=-0 and y%2=-0 and z%2=-0 and d%2==0:
            return d