def qtd_divisores(n):
    """ Função que retorna a quantidade de divisores que um número n tem.
    int --> int"""
    if n < 0:
        return 0
    soma_divisores = 0
    for numero in range (1, n):
        if (n % numero) == 0:
            soma_divisores += 1 
    return soma_divisores + 1