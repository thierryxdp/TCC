def qtd_divisores(numero):
    '''recebe um numero e retorna a qtd de divisores'''
    i=0
    for i in range(1, numero//2+1):
        if numero % i == 0:
            return i
    return numero