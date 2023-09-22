def qtd_divisores(n):
    s=0
    for i in range(n) and i!=0:
        if n%i==0:
            s=s+1
    return s