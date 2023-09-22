def filtra_pares(x1,x2,x3,x4):
    """função que retorna apenas as tuplas pares
    tuple, tuple, tuple, tuple -> tuple"""
    if (x1%2==0) and (x2%2==0) and (x3%2==0) and (x4%2==0):
        return (x1,x2,x3,x4)