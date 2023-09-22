def qtd_divisores(n):
    div=map(lambda x: x if n%i==0 else None,range(1,n+1))
    return sum(div)