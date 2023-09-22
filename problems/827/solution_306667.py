def qtd_divisores(n):
    '''retorna a quantidade de divisores de n; int -> int'''
    samara = 0
    for i in range(n):
        if i == 0:
            samara += 0
        else n%i == 0:
            samara += 1
    return samara