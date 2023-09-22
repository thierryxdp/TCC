def fatorial(n):
    q = 1

    for i in range(n + 1)[1:]:
        q *= i

    return q

print(fatorial(8))