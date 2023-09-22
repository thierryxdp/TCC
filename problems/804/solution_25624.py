def filtra_pares(tupla):
    nova_tupla = ()
    if (tupla[0] % 2 == 0):
        nova_tupla[0] = tupla[0]
    if (tupla[1] % 2 == 0):
        nova_tupla[1] = tupla[1]
    if (tupla[2] % 2 == 0):
        nova_tupla[2] = tupla[2]
    if (tupla[3] % 2 == 0):
        nova_tupla[3] = tupla[3]
        
    return nova_tupla