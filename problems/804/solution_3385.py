def filtra_pares(t):
    """ função que receba uma tupla com 4 elementos inteiros e retorne uma nova tupla contendo apenas os elementos pares"""
    x,y,z,w=t
    if x%2== 0 and y%2==0:
        return str(str(x)+","+str(y))
    elif x%2== 0 and z%2==0:
        return str(str(x)+","+str(z))
    elif x%2== 0 and w%2==0:
        return str(str(x)+","+str(w))
    elif y%2== 0 and z%2==0:
        return str(str(y)+","+str(z))
    elif y%2== 0 and w%2==0:
        return str(str(y)+","+str(w))
    elif z%2== 0 and w%2==0:
        return str(str(z)+","+str(w))
    elif x%2== 0 and y%2==0 and z%2==0:
        return str(str(x)+ "," +str(y)","+str(z))
    elif x%2== 0 and y%2==0 and w%2==0:
        return str(str(x)+","+str(y)","+str(w))
    elif w%2== 0 and y%2==0 and z%2==0:
        return str(str(w)+","+str(y)","+str(z))
    elif x%2== 0 and y%2==0 and z%==0 and w%2==0:
        return str(str(x)+","+str(y)","+str(z)","+str(w))