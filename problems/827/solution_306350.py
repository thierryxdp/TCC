def qtd_divisores(n):
    ''' conta a quantidade de divisores de um número
    int -> int'''
    if n < 0:
        return 0
    divisores = list(range(1,1000))
    quantidade = 0
    for numero in divisores:
        if n % numero == 0:
            quantidade = quantidade + 1
    return quantidade