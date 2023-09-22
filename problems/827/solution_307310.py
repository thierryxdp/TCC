def qtd_divisores (n):
    for i in range(1, num // 2 + 1):
        if num % i == 0: 
            yield i
    yield num