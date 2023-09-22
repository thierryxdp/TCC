def qtd_divisores(n):
    total=0
    for x in range(n):
        if (x+1)%n==0:
            total+=1
    return total