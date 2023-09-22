def qtd_divisores(n):
    quantos = 0
    for x in range(0, n+1):
        if n%x==0:
            quantos += 1
            
    return quantos