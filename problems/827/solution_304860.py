def qtd_divisores(n):
    l = []
    c = 1
    while n <= c:
        if n % c == 0:
            l = list.append(l, c)
    return len(l)