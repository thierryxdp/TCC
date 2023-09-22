def qtd_divisores(n):
    return len([i for i in range(2, n, ) if n%i==0])+2