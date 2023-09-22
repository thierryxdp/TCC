def qtd_divisores(n):
    l = []
    for c in range(n) :
        if n % c == 0:
            l = list.append(l, n % c)
    return len(l)