def qtd_divisores(num):
    ''''''
    soma = 0
    for n in range(num):
        if num % n == 0:
            soma += 1
    return soma + 1