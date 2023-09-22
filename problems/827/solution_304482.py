def qtd_divisores(n):
    i=0
    acum=0
    while i<=n :
        if  n%i==0 :
        acum=acum+1
    i=i+1
    return acum