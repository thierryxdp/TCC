def qtd_divisores(n):
    div=[]
    for i in range(1,n+1):
        if (n % i) == 0:
            list.append(div, i)
    return len(div)