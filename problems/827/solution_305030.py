def qtd_divisores(n):
    """função que calcula a quantidade de divisores
    que um número n, passado como parâmetro, possui
    int -> int"""
    qtd = 0
    for i in range(1,n+1):
        if n%i == 0:
            qtd += 1
    return qtd