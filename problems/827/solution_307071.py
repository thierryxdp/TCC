def qtd_divisores(numero):
    '''recebe um numero inteiro como entrada e retorna o numero de divisores;
    int -> int'''
    quantidade = 0
    for divisor in range(1, numero+1):
        if numero%divisor == 0:
            quantidade += 1
    return quantidade