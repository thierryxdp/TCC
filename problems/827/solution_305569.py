def qtd_divisores(num):
    '''Calcula o número de divisores de um número
    int -> int'''
    k = 0
    div = list(range(1, num+1))
    for i in div:
        if num%i == 0:
            k += 1
    return k