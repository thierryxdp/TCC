def filtra_pares (tupla):
    '''função que recebe um tupla e devolve somente seus numeros pares; tupla->tupla'''
    if tupla[0]%2==0:
        return (tupla[0],)
    elif tupla[1]%2==0:
        return (,tupla[1])