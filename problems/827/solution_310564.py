def qtd_divisores(n):
    x = 0
    for r in range(1,n//2+1):
        if n%r == 0:
            x = x+1
    if n == 0 or n<0:
        return 0
    else:
        return x+1