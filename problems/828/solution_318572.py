def primo(x):
    '''função que dado um numero, verifica se este número é primo. Retornando verdadeiro ou falso'''
    divisores = 0
    for numero in range(1, x + 1):
        if x % numero == 0:
            divisores = divisores+1
    return divisores==2