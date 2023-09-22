def qtd_divisores(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l = list.append(l, i)
    return l