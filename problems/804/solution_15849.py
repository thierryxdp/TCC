def tup0t(tup):
    return tup[0]%2 ==0

def tup1t(tup):
    return tup[1]%2 ==0

def tup2t(tup):
    return tup[2]%2 ==0

def tup3t(tup):
    return tup[3]%2 ==0

def filtra_pares(tup):
    """ A função filtra elementos que são pares
    e os direciona em uma nova tupla
    tup -> tup """
    ftup=()
    if tup0t(tup):
        ftup = ftup + (tup[0],)
    if tup1t(tup):
        ftup = ftup + (tup[1],)
    if tup2t(tup):
        ftup = ftup + (tup[2],)
    if tup3t(tup):
        ftup = ftup + (tup[3],)
    return ftup