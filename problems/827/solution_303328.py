def qtd_divisores(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0 :
            soma = soma + i
        else:
            continue 
    return soma