def filtra_pares (t):
    """ recebe uma tupla 't' de quatro elementos e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    tuple -> tuple """
    t= (t[0],t[1],t[2],t[3])
    pares=()
    
    for t[0] in t:
        if t[0]%2==0:
            pares.append(t[0])
    for t[1] in t:
        if t[1]%2==0:
            pares.append(t[1])
    for t[2] in t:
        if t[2]%2==0:
            pares.append(t[2])
    for t[3] in t:
        if t[3]%2==0:
            pares.append(t[3])
            return pares