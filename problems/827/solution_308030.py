def qtd_divisores(n):
    
    if n < 0:
        return 0
    soma = 0
    for num in range(1,n):
        if(n % num) == 0:
            soma += 1
    return soma+1