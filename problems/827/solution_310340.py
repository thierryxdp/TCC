def qtd_divisores(n):
    if n<=0:
        return 0
    return len([i for i in range(2, abs(n)) if n%i==0])+2