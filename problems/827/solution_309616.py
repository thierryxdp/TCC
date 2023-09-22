def qtd_divisores(n):
    '''
    Funçao que recebe um numero e retorna quantos divisores ele tem
    int -> str
    '''
    divisores = 0
    for i < n:
        if n%i == 0:
            divisores = divisores + 1
    return str(n) + ' tem ' + str(divisores) + 'divisores. '