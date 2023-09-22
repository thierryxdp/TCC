def filtra_pares(tupla): 
    """Retorna uma nova tupla contendo somente os elementos
    pares da tupla antiga;
    tuple -> tuple"""
    nova_tupla = []
    if tupla[0] % 2 == 0:
        nova_tupla= tupla[0]
    if tupla[1] % 2 == 0:
        nova_tupla = [nova_tupla] + [tupla[1]]
    if tupla[2] % 2 == 0:
        nova_tupla = [nova_tupla] + [tupla[2]
    if tupla[3] % 2 == 0:
        nova_tupla = [nova_tupla] + [tupla[3]]

    return tuple((nova_tupla))