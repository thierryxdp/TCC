def filtra_pares(e1,e2,e3,e4):
    """"""
    elementos=e1+e2+e3+e4
    elementos=list(filter(lambda x:x%2==0,elementos)) 
    return elementos