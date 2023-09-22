def filtra_pares(t):
    '''função deverá retornar os valores pares
    da tupla'''
    nova_tupla=tuple()
    if t[0]%2== 0:
        nova_tuple=nova_tuple+(t[0],)
    if t[1]%2== 0:
        nova_tuple=nova_tuple+(t[1],)
    if t[2]%2== 0:
        nova_tuple=nova_tuple+(t[2],)
    if t[3]%2== 0:
        nova_tuple=nova_tuple+(t[3],)
        return nova_tuple