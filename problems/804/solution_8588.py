def filtra_pares(a,b,c,d):
    
    A = int(str(a / 2)[-1])
    B = int(str(b / 2)[-1])
    C = int(str(c / 2)[-1])
    D = int(str(d / 2)[-1])
    
    tupla_nova = (A,B,C,D)
    
    if tupla_nova == (0,0,0,0):
        return (a,b,c,d)
    if tupla_nova == (0,0,0,5):
        return (a,b,c)
    if tupla_nova == (0,0,5,5):
        return (a,b)
    if tupla_nova == (0,5,5,5):
        return (a)
    if tupla_nova == (5,5,5,5):
        return tuple()