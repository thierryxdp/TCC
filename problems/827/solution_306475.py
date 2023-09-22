def qtd_divisores(n):
    div=filter(lambda x: 1 if n%x==0 else 0,range(1,n+1))
    s=map(lambda x: 1 if div!=0 else 0,div)
    return sum(s)