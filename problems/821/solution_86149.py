def fatorial (n):
    fatorial = 1
    count = 1
    while count <= n:
        fatorial *= count
        count += 1
    return (fatorial)