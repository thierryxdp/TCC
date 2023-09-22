def conta_numero(n,m):
    p=0
    quantidade=0
    for elemento in m:
        quantidade=quantidade+list.count(m[elemento],n)
        p=p+1
    return quantidade