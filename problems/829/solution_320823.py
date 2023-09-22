def soma_h(numero):
    '''função que recebe um numero e retorn o valor H
    com n termos'''
    soma = 0
    for i in range(1, numero+1):
        soma = soma + 1/i
    return round(soma, 2)