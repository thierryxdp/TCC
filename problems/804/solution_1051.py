def filtra_pares(tup):
    """coment"""
    num_par=[]
    tup=(n1,n2,n3,n4)
    for i in tup:
        if i%2==0:
            num_par.append(i)
            return num_par