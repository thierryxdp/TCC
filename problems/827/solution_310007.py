def qtd_divisores(n):
    r = []
    for i in range(n+1):
        if n%i==0:
            r.append i
    return r