def qtd_divisores(m):
    d=0
    for i in range(m):
       if m%i==0:
        d=d +1
    return d