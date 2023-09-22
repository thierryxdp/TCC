def filtra_pares(tup):
    '''tuple(int,int,int,int) -> tuple'''
    x=()
    if tup[0]%2==0:
        return x+tup[0]
    if tup[1]%2==0:
        return x+tup[1]