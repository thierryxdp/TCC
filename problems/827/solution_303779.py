def qtd_divisores(n):
    m= (n//2)
    div=[]
    for i in range(1,m):
        if (n % i) == 0:
            div = list.append(div, i)
    return len(div)