def qtd_divisores(n):
    i = 1
    divisores = []
    while i <= n:
        if n%i == 0:
            list.append(divisores, i)
        i = i + 1
    return len(divisores)+1