def qtd_divisores(n):
    divisores=[]
    for i in range(1,n+1):
        if (n%i) == 0:
            list.append(divisores,i)
    return len(divisores)