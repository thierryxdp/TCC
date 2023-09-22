def qtd_divisores(num):
    n = 1
    a = []
    if num < 0:
        return 0
    while n < num:
        if num%n == 0:
            a = a + [n]
        n = n + 1
    return len(a)+1