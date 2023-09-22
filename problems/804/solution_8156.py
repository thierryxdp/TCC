def filtra_pares(t1, t2, t3, t4):
    """retorna uma nova tupla contendo apenas os elementos pares da tupla original sendo t1,t2,t3,t4 elementos da tupla original.
    int,int,int,int-> tupla"""
    if t1%2==0:
        return (t1,)
    elif t2%2==0:
        return (t1,) + (t2,)
    elif t3%2==0:
        return (t1,) + (t2,) + (t3,)
    elif t4%2==0:
        return (t1,) + (t2,) + (t3,) + (t4,)
    else:
        return ()