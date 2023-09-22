def qtd_divisores(n):
    div = 0
    for e in range(1, (n + 1)):
        if n % e == 0:
            div += 1
    return div