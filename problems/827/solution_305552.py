def qtd_divisores(n):
    '''Funcao que dado um numero "n", conta quantos divisores
    ele tem
    int -> int'''
    divisores = []
    for elemento in range(1, n+1):
        if n%elemento==0:
            divisores = divisores + [elemento]
    return len(divisores)