def qtd_divisores(numero):
    '''Conta quantos divisores um número possui;
    int -> int'''
    
    divisores = 0
    for contador in range(1, numero + 1):
        if numero % contador == 0:
            divisores += 1
    return divisores