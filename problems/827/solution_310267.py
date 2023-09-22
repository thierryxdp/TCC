def qtd_divisores(n):
    total = 2
    sup = int(round(n/2))
    for i in range(2,sup):
        if n%i == 0:
            total = total + 1
    
    return total