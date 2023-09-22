def filtra_pares(a,b,c,d):
    if a%2 == 0:
    aepar = True
    if b%2 ==0:
    bepar == True
    if c%2 ==0:
    cepar == True
    if d%2 ==0:
    depar ==True
    if aepar ==True and bepar == True and cepar == True and depar == True
    return (a,b,c,d)
    if aepar ==True and bepar == True and cepar == True and depar == False
    return (a,b,c)
    if aepar ==True and bepar == True and cepar == False and depar == False
    return (a,b)
    if aepar ==True and bepar == False and cepar == True and depar == False
    return (a,c)
    if aepar ==True and bepar == False and cepar == False and depar == True
    return (a,d)
    if aepar ==True and bepar == False and cepar == True and depar == True
    return (a,c,d)
    if aepar == True and bepar == True and cepar == False and depar == True
    return (a,b,d)
    if aepar ==False and bepar == True and cepar == True and depar == True
    return (b,c,d)
    if aepar ==False and bepar == True and cepar == True and depar == False
    return (b,c)
    if aepar ==False and bepar == True and cepar == False and depar == True
    return (b,d)
    if aepar ==False and bepar == False and cepar == True and depar == True
    return (c,d)