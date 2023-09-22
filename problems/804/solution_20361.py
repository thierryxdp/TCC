def filtra_pares(a,b,c,d):
    da=a%2
    db=b%2
    dc=c%2
    dd=d%2
    if da==0:
        tupla_a=(a,)
    else:
        tupla_a=()
    if db==0:
        tupla_b=(b,)
    else:
        tupla_b=()
    if dc==0:
        tupla_c=(c,)
    else:
        tupla_c=()
    if dd==0:
        tupla_d=(d,)
    else:
        tupla_d=()
    return tupla_a+tupla_b+tupla_c+tupla_d