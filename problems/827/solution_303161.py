def qtd_divisores(n):
    divisores_count = []
    for i in range(1,n+1):
        if not(n%i):
            divisores_count.append(i)
    return len(divisores_count)