def qtd_divisores(n):
    div=map(lambda x: 1 if n%x==0 else 0,range(1,n+1))
    return sum(div)