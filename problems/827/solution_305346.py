def qtd_divisores(n):
    '''Entre com um numero para saber quantos divisores ele tem
    Int -> Int'''
    soma=0
    for x in range(n+1):
        if x<n:
            if n%x == 0:
                soma=soma+1
    return soma