def filtra_pares(x):
    'dada uma tupla de 4 elementos, retorna uma tupla contendo apenas os elementos pares da original tuple -> tuple'
    x1=[]
    if x[0]//2==0 :
        x1=x1+[x[0]]
        return tuple(x1)