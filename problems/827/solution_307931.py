def qtd_divisores(n):
    count = 2  
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if i ** 2 == n:
        count += 1
    else:
        count == 0
    return count