def filtra_pares(x):
    """funcao que retorna uma tupla contendo apenas os elementos pares
       dentre os elementos inseridos na mesma ordem em que estavam
       
       int,int,int,int-> tupla
    """

    a = x[0]
    b = x[2]
    c = x[3]
    d = x[4]
    
    if (a%2, b%2, c%2, d%2)== (0,0,0,0):
        return (a,b,c,d)
    if (a%2, b%2, c%2, d%2)== (0,0,0,1):
        return (a,b,c)
    if (a%2, b%2, c%2, d%2)== (0,0,1,0):
        return (a,b,d)
    if (a%2, b%2, c%2, d%2)== (0,1,0,0):
        return (a,c,d)
    if (a%2, b%2, c%2, d%2)== (1,0,0,0):
        return (b,c,d)
    if (a%2, b%2, c%2, d%2)== (1,1,0,0):
        return (c,d)
    if (a%2, b%2, c%2, d%2)== (1,0,1,0):
        return (b,d)
    if (a%2, b%2, c%2, d%2)== (1,0,0,1):
        return (b,c)
    if (a%2, b%2, c%2, d%2)== (0,1,1,0):
        return (a,d)
    if (a%2, b%2, c%2, d%2)== (0,1,0,1):
        return (a,c)
    if (a%2, b%2, c%2, d%2)== (1,1,1,0):
        return (d)
    if (a%2, b%2, c%2, d%2)== (1,1,0,1):
        return (c)
    if (a%2, b%2, c%2, d%2)== (1,0,1,1):
        return (b)
    if (a%2, b%2, c%2, d%2)== (0,1,1,1):
        return (a)