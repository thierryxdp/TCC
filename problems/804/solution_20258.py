def filtra_pares(e):
    pares_novo=[]
    if e[0]%2==0:
        pares_novo.insert(0,e[0])
    if e[1]%2==0:
        pares_novo.insert(1,e[1])
    if e[2]%2==0:
        pares_novo.insert(2,e[2])
    if e[3]%2==0:
        pares_novo.insert(3,e[3])
    return tuple(pares_novo)