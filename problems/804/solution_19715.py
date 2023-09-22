def filtra_pares (tupla):
    '''função que recebe uma tupla e devolve só os seus elementos pares; tuple->tuple''''
    tupla==()
    if tupla[0]%2==0:
        return tupla = tupla+(tupla[0],)
    if tupla[1]%2==0:
        return tupla = tupla+(tupla[1],)
    if tupla[2]%2==0:
       	return tupla = tupla+(tupla[2],)
    if tupla[3]%2==0:
        return tupla = tupla+(tupla[3])
    else:
    	return ()