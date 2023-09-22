def qtd_divisores(n):
    quantos = 0
    for n in range(0, n+1):
        if n%10==0:
            quantos += 1
            
    return quantos