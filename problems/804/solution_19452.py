def filtra_pares(a,b,c,d):
    pares_novo=[]
    if a%2==0:
        pares_novo.insert(0,a)
    if b%2==0:
        pares_novo.insert(1,b)
    if a%2==0:
        pares_novo.insert(2,c)
    if b%2==0:
        pares_novo.insert(3,d)
    return pares_novo