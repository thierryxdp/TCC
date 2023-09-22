def filtra_pares (tupla):
    '''função que recebe uma tupla e devolve só os seus elementos pares; tupla->tupla'''
    tupla=(a,b,c,d)
    if p[0]%2==0:
        tupla=tupla+(p[0],)
    if p[1]%2==0:
        tupla=tupla+(p[1],)
    if p[2]%2==0:
        tupla=tupla+(p[2],)
    if p[3]%2==0:
        tupla=tupla+(p[3],)
    return tupla