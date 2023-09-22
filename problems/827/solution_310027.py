def qtd_divisores(n):
    l=list(range(n))
    total=int
    for x in l:
        if n%x==0:
            total=total+1
    return total