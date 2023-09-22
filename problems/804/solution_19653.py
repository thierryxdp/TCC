def filtra_pares (tupla):
    '''função que recebe um tupla e devolve somente seus numeros pares; tupla->tupla'''
    if (tupla[0]%2==0, tupla[1]%2==0,tupla[2]%2,tupla[3]%2==0==0):
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    elif tupla[1]%2==0:
        return (tupla[1],)
    elif tupla[2]%2==0:
        return(tupla[2],)
    elif tupla[3]%2==0:
        return(tupla[3])
    else:
        return()