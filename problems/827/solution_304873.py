def qtd_divisores(n):
    l = []
    c = 0
    while c <= n :
        if n % c == 0:
            l = list.append(l, n % c)
    return len(l)