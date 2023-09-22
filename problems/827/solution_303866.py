def qtd_divisores(n):
    '''Função que conta quantos divisores um dado número inteiro tem.
    int-->int'''
    contador = 0
    for i in range(1,n+1):
        if (n % i == 0):
            contador = contador + 1
    return contador