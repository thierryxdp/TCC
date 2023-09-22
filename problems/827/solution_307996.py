def qtd_divisores(n):
    divisores=0
    for x in range(1,n+1):
        if n%x==0:
            divisores= divisores+x