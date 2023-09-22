def filtra_pares(tupla):
    pares=[]
    if tupla[0]%2==0:
        tupla[0].append(pares)
    if tupla[1]%2==0:
        tupla[1].append(pares)
    if tupla[2]%2==0:
        tupla[2].append(pares)
    if tupla[3]%2==0:
        tupla[3].append(pares)
    final=tuple(pares)
    return final