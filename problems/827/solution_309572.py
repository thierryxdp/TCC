def qtd_divisores(numero):
    '''
    função que conta quantos divisores um número tem;
    int -> int
    '''
    soma = 0
    for num in range(1,numero+1):
        if numero%num == 0:
            soma = soma + 1
    return soma