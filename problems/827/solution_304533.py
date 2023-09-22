def qtd_divisores(n):
    '''função que dado um inteiro, retorna a quantidade de divisores deste número. int -> int'''
    acumulador = 0
    for num in range(n):
        if n % num == 0:
            acumulador = acumulador + 1
    return acumulador