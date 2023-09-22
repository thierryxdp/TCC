def qtd_divisores(n):
    '''função que retorna a quantidade de divisores de um número inteiro n;
    int --> int'''
    i = 0
    for num in range(1,n+1):
        if n % num == 0:
            i = i + 1
    return i