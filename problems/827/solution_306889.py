def qtd_divisores(n):
    """ Função que dados um número inteiro, retorna a quantidade
    de seus divisores
    int -> int"""
    x = 0
    for y in range(1, n+1):
        if n%y == 0:
            x+= 1
    return x