def qtd_divisores(n):
    '''Calcula a quantidade de divisores de n
    int --> int'''

    # variável para guardar o total de divisores de n
    total = 0

    # itera no intervalo de 1 até n
    for i in range(1, n+1):
        # verifica se i é divisor de n
        if n % i == 0:
            # incrementa o total em uma unidade
            total += 1
    return total