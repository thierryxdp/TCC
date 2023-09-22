def qtd_divisores (n):
    soma = 0
    for i in range(1, n+1):
        if i%n == 0: 
            soma+i
    return soma