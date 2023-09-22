def qtd_divisores(numero):
    '''funçao que conta quantos divisores um numero tem;
    int -> int'''
    conta=0
    for i in range(1,numero+1):
        if numero % i==0:
            conta= conta + 1
    return conta