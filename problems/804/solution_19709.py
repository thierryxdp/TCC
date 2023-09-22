def filtra_pares (tupla):
    '''função que recebe uma tupla e devolve só os seus elementos pares; tuple->tuple''''
    tupla==()
    if tupla[0]%2==0:
        return tupla+(tupla[0],)