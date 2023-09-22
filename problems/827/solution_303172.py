# Divisores
def qtd_divisores(n):
    '''Essa função recebe um número n e retorna a quantidade de divisores
    que ele possui;
    INT -> INT'''
    conta = 0
    for i in range(1,n+1):
        if n%i == 0:
            conta += 1
    return conta