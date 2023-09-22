def soma_h(n):
    '''recebe um inteiro e calcula o valor de H, retornando um valor flutuante com 2 casas decimais
    int -> float
    '''
    H = 1
    i = 2
    while (i <= n):
        H += 1/i
        i += 1
    return round(H,2)