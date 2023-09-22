def qtd_divisores(n):
    '''Dado um número retorna sua quantidade de divisores
    int -> int'''
    dvs = []
    for i in range(n,0,-1):
        if n % i == 0:
            dvs.append(i)
    return len(dvs)