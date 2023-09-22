def filtra_pares(n1,n2,n3,n4):
    todos = ((n1),(n2),(n3),(n4))
    pares = ()
    if n1 %2==0:
        return pares + n1
    if n2 %2==0:
        return pares + n2
    if n3 %2==0:
        return pares + n3
    if n4 %2==0:
        return pares + n4
    else:
        return 'NDA'