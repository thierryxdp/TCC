def qtd_divisores(n):
    """ Função que conta o número de divisores.
    int, int->int """
    total = 0
    qtd = 1
    for i in range(1,n+1):
        if  n% 2 = 0:
            total = total + qtd
            qtd = qtd*i
    return total