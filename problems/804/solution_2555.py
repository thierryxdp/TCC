def filtra_pares (t):
    """ recebe uma tupla 't' de quatro elementos e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    tuple -> tuple """
    t= (t[0],t[1],t[2],t[3])
    pares=()
    
    if t[0]%2==0:
        pares +=(t[0],)
        elif t[1]%2==0:
            pares +=(t[1],)
            elif t[2]%2==0:
                pares +=(t[2],)
                elif t[3]%2==0:
                    pares +=(t[3],)
                    return pares