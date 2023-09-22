def filtra_pares(p):
    """retorne os números pares da tupla de entrada"""
    novos_pares=[]
    if p[0]%2==0:
        novos_pares.insert(0,p[0])
    if p[1]%2==0:
        novos_pares.insert(1,p[1])
    if p[2]%2==0:
        novos_pares.insert(2,p[2])
    if p[3]%2==0:
        novos_pares.insert(3,p[3])
    return tuple(novos_pares)