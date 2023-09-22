def filtra_pares(*n):
    num = n
    for n in num:
        if n % 2 == 0:
            print(n, end=' ')