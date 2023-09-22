def filtra_pares(tupla):
    """filtra os pares das tuplas de entrada"""
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return tupla
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and not (tupla[3]%2==0):
        return tupla[0,1,2]
    if tupla[0]%2==0 and tupla[1]%2==0 and not( tupla[2]%2==0 and tupla[3]%2==0):
        return tupla[0,1]
    if tupla[0]%2==0 and not (tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0):
        return tupla[0]
    else:
        return tupla()