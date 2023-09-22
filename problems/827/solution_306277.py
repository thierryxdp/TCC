def qtd_divisores(num):
    ''''''
    soma = 0
    for n in range(num):
        if n % num == 0:
            soma += 1
    return soma