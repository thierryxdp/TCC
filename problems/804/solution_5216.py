def filtra_pares(A):
    """retorna apenas os elementos pares da tupla original
    tuple -> tuple"""
    if A[0]%2 == 0 and A[1]%2 == 0 and A[2]%2 == 0 and A[3]%2 == 0:
        return A
    elif A[0]%2 == 0 and A[1]%2 == 0 and A[2]%2 == 0:
        return (A[0],A[1],A[2])
    elif A[0]%2 == 0 and A[1]%2 == 0 and A[3]%2 == 0:
        return (A[0],A[1],A[3])
    elif A[0]%2 == 0 and A[2]%2 == 0 and A[3]%2 == 0:
    	return (A[0],A[2],A[3])
    elif A[1]%2 == 0 and A[2]%2 == 0 and A[2]%2 == 0:
        return (A[1],A[2],A[3])
    elif A[0]%2 == 0 and A[1]%2 == 0:
        return (A[0],A[1])
    elif A[0]%2 == 0 and A[2]%2 == 0:
        return (A[0],A[2])
    elif A[0]%2 == 0 and A[3]%2 == 0:
        return (A[0],A[3])
    elif A[1]%2 == 0 and A[2]%2 == 0:
        return (A[1],A[2])
    elif A[1]%2 == 0 and A[3]%2 == 0:
        return (A[1],A[3])
    elif A[2]%2 == 0 and A[3]%2 == 0:
        return (A[2],A[3])
    elif A[0]%2 == 0:
        return (A[0],)
    elif A[1]%2 == 0:
        return (A[1],)
    elif A[2]%2 == 0:
        return (A[2],)
    elif A[3]%2 == 0:
        return (A[3],)
    else:
    	return ()