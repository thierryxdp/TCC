def qtd_divisores(numero):
    '''essa função irá contar quantos divisores um numero tem.
    entrada -> int
    saida -> int '''
    
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    
    return divisores