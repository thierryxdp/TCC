def qtd_divisores(n):
    '''
    Função que conta quantos divisores um número tem.
    int -> int
    '''
    total = 0
    for num in range(1, (n + 1)):
        if n % num == 0 and n > 0:
            total = total + 1
            
    return total