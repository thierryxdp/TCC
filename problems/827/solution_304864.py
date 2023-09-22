def qtd_divisores(n):
    l = []
    c = 1
    while c <= n :
        if n % c == 0:
            l = list.append(l, c)
    return len(l)