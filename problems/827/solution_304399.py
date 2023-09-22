def qtd_divisores(n):
    total = 0
    for contador in range(1,n+1):
        if n%contador == 0:
            total += 1
    return total