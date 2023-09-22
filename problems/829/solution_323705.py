def soma_h(numero):
    '''Função que retorne o valor com N termos, int -> float'''
    somatorio = 0
    for x range(1, numero):
        fracao = 1/numero
        somatorio = somatorio + fracao
    return round(somatorio, 2)