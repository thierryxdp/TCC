def qtd_divisores(n):
    soma = 0
    for i in range(1, n+1):
        if n % i == 0 :
            soma = soma + 1
        else:
            continue 
    return soma