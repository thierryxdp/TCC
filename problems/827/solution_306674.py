def qtd_divisores(n):
    '''retorna a quantidade de divisores de n; int -> int'''
    samara = 0
    for i in range(n+1):
        if i == 0:
            samara = samara + 0
        elif n%i == 0:
            samara = samara + 1
    return samara