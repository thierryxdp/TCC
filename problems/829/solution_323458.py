def soma_h(N):
    '''Uma função que calcula e retorna o valor H de uma funcão com N
    termos, sendo H= 1+ 1/2 + 1/3 + ... + 1/n
    int -> float'''
    soma = 0
    for i in N:
        soma += 1/i
    return round(soma, 2)