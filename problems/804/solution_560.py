def filtra_pares((n1,n2,n3,n4)):
    """coment"""
    tup=(n1,n2,n3,n4)
    for i in range tup:
        if tup[i]%2 != 0:
            tup.remove(tup[i])
            return tup