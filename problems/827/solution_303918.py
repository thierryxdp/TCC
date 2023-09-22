def qtd_divisores(n):
    """ Função que conta o número de divisores.
    int, int->int """
    total = 0
    for i in range(1,n+1,1):
        if  n% i==0:
            total = total + 1
    return total