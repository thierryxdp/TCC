def qtd_divisores(n):
    l = []
    for c in range(n/2+1) :
        if n % c == 0:
            l = list.append(l, n % c)
    return len(l)