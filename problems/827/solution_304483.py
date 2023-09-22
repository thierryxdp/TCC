def qtd_divisores(n):
    i=1
    acum=1
    while i<=n :
        if  n%i==0 :
        acum=acum+1
    i=i+1
    return acum