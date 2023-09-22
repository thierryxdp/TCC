def soma_h(n):
    '''recebe um inteiro e calcula o valor de H, retornando um valor flutuante com 2 casas decimais
    int -> float
    '''
    H = 0
    i = 1
    for i in range(n):
        H += 1/(i+1)
        i += 1
    return round(H,2)