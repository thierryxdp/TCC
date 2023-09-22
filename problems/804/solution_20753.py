def filtra_pares(x):
    'dada uma tupla de 4 elementos, retorna uma tupla contendo apenas os elementos pares da original tuple -> tuple'
    for j in range(4):
        x1=[]
        if x[1]%2==0:
            x1= x1 + [x[j]]
        return tuple(x1)