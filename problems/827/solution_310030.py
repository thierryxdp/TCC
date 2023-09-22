def qtd_divisores(n):
    l=list(range(n))
    total=int
    for x in l[1:]:
        if n%x==0:
            total+=1
    return total