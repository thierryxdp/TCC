def qtd_divisores(n):
    s=0
    for i in range(n+1):
        if i==0:
            s=s
        elif n%i==0:
            s=s+1
    return s