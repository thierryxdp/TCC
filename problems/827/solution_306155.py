def qtd_divisores(n):
    divisores = []
    for elementos in range(1, n+1):
        if n % elementos == 0:
            list.append(divisores, elementos)
    return len(divisores)