def qtd_divisores(num):
    n = 1
    a = []
    while n < num:
        if num%n == 0:
            a = a + [n]
        n = n + 1
    return len(n)