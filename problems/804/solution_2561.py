def filtra_pares(t):
    '''dada uma tupla com quatro elementos inteiros, retorna uma nova tupla somente com os elementos pares;
    tuple --> tuple'''
    if t[0]%2==0:
        if t[1]%2==0:
            if t[2]%2==0:
                if t[3]%2==0:
                    return (t[0],t[1],t[2],t[3])
                else:
                    return (t[0],t[1],t[2])
            else:
                if t[3]%2==0:
                    return (t[0],t[1],t[3])
                else:
                    return (t[0],t[1])
        else:
            if t[2]%2==0:
                if t[3]%2==0:
                    return (t[0],t[2],t[3])
                else:
                    return (t[0],t[2])
            else:
                if t[3]%2==0:
                    return (t[0],t[3])
                else:
                    return (t[0],)
    else:
        if t[1]%2==0:
            if t[2]%2==0:
                if t[3]%2==0:
                    return (t[1],t[2],t[3])
                else:
                    return (t[1],t[2])
            else:
                if t[3]%2==0:
                    return (t[1],t[3])
                else:
                    return (t[1],)
        else:
            if t[2]%2==0:
                if t[3]%2==0:
                    return (t[2],t[3])
                else:
                    return (t[2],)
            else:
                if t[3]%2==0:
                    return (t[3],)
                else:
                    return ()