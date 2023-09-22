def filtra_pares ([n1, n2, n3, n4]):
# int, int, int, int -> tuple(...)
    if par (n1):
        return (n1,)
    elif par (n2,):
        return r + (n2,)
    elif par (n3,):
        return r + (n3,)
    elif par (n4,):
        return r + (n4,)
    else:
        return ()
    
    def par (n):
        return n % 2 == 0