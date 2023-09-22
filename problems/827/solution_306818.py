def qtd_divisores(n):
    ''''''
    divisores=[]
    for x in range(1,n+1):
        if n%x == 0:
            list.append(divisores, x)
    return len(divisores)