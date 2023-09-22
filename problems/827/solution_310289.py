def qtd_divisores(n):
    '''Função que dado um nº inteiro retorna a quantidade de divisores que
este nº tem.
int, float -> int'''
    divi = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divi += 1
    return divi