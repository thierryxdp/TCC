def qtd_divisores(n):
    """ Função que conte quantos divisores um número tem,
    int --> int"""
    cont = 0 
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    return cont