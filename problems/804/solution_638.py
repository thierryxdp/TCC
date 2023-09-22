def filtra_pares(n1,n2,n3,n4):
    """coment"""
    lis = [n1, n2, n3, n4]
    res=[]
    for n in lis:
        if n % 2 == 0:
            res.append(n)