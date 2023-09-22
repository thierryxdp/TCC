def qtd_divisores(m):
    d=0
    for i in range(m/2):
       if m%i==0:
        d=d +1
    return d