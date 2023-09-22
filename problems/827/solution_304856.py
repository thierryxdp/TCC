def qtd_divisores(n):
    l = []
    for c in range(1//1+3):
        if n % c == 0:
            l = list.append(l, c)
    return len(l)