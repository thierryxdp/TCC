def qtd_divisores(n):
    a = []
    i = 1
    while i <= n:
        if n%i == 0:
            a = a + [i]
        i = i + 1
    return len(a)