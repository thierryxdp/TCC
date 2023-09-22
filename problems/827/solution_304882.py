def qtd_divisores(n):
    l = []
    c = 1
    while c <= n:
        if n % c == 0:
            l = list.append(l, n % c)
            c = c + 1
    return len(l)