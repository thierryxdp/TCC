def qtd_divisores(n):
    result = 0
    sqrt_n = int(pown,0.5)

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            result += 1

    result *= 2

    if sqrt_n**2 == n:
        result -= 1

    return result