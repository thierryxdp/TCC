def qtd_divisores(n):
    cont = 0
    for c in range(1, n + 1):
        if n % c == 0:
            cont += 1
    return cont