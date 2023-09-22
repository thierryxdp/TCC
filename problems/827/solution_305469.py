def qtd_divisores(n):
    quantos = 0
    for a in range(0, n+1):
        if n%a==0:
            quantos += 1
            
    return quantos