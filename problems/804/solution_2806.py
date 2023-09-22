def filtra_pares(tupla):
    """filtra os pares das tuplas de entrada"""
    if tupla[0]%2==0:
        return tupla[0]
    if tupla[1]%2==0:
        return tupla[1]
    if tupla[2]%2==0:
        return tupla[2]
    if tupla[3]%2==0:
        return tupla[3]
    else:
        return tupla()