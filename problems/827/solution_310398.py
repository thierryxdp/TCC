def qtd_divisores(x):
    '''função que dado um numero, retorna quantos dividores ele possue''' 
    divisores = 0
    for numero in range(1, x + 1):
        if x % numero == 0:
            divisores = divisores+1
    return divisores