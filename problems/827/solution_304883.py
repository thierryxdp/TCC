def qtd_divisores(n):
    l = []
    c = 1
    while c <= n:
        if n % c == 0:
            n % c = r
            l = list.append(l, r)
            c = c + 1
    return len(l)