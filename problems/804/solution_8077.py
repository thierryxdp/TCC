def filtra_pares(num):
    pares = ()
    if (num[0],[1],[2],[3]) %2==0:
        return pares + (num[0],[1],[2],[3])
    elif num[0] %2==0:
        return  pares + (num[0],)
    elif num[1] %2==0:
        return  pares + (num[1],)
    elif num[2] %2==0:
        return  pares + (num[2],)
    elif num[3] %2==0:
        return pares + (num[3],)
    else:
        return pares