def qtd_divisores(n):
    if n <= 0:
        return 0
    total = 1
    for contador in range(1,n//2+1):
        if n%contador == 0:
            total += 1
    return total