def qtd_divisores(n):
    divisores=[]
    for a in range(1,n+1):
        if n%a==0:
            divisores=divisores+[a,]
            a=a+1
    return len(divisores)