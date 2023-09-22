def filtra_pares(a,b,c,d):
    '''Funçao que apenas retorna os numeros pares 
    presentes no conjunto inicial
    int,int,int,int -> tuple'''
    pares=()
    if a%2==0:
        pares.append(a)
    else:
        pares=pares
    if b%2==0:
        pares.append(b)
    else:
        pares=pares
    if c%2==0:
        pares.append(c)
    else:
        pares=pares
    if d%2==0:
        pares.append(d)
    else:
        pares=pares
    return pares