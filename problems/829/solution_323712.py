def soma_h(numero):
    '''Função que retorne o valor com N termos, int -> float'''
    somatorio = 0
    for x in range(1, numero + 1):
        fracao = 1/x
        somatorio = somatorio + fracao
    return round(somatorio, 2)