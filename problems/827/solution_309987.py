def qtd_divisores (n):
    total = 0
    for i in range(1,n+1):
        total = total*(i+1)
    return total