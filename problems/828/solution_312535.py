def divisores(n):
    qtd_divisores = 0
    for numero in range(1,n+1):
        if n%numero == 0:
            qtd_divisores += 1
        else:
            pass
        return qtd_divisores