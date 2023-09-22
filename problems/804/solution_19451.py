def filtra_pares(a,b,c,d):
    pares_novo=[]
    if a%2==0:
        pares_novo.insert(0,str(a))
    if b%2==0:
        pares_novo.insert(1,str(b))
    if a%2==0:
        pares_novo.insert(2,str(c))
    if b%2==0:
        pares_novo.insert(3,str(d))
    return pares_novo