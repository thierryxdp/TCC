def filtra_pares(tupla):
    """"""
    tupla=list(filter(lambda x:x%2==0,tupla)) 
    return '('+tupla+')'