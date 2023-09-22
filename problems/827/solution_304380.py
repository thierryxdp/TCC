def qtd_divisores(n):
    '''funcao que conta quantos divisores um numero passado como entrada possui
    float -> int'''
    contador = 0
    for i in range(1, n+1):
        if ((n % i) == 0):
            contador += 1
    return contador