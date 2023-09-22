def soma_h(N):
    '''Função que calcula a soma h para N termos.
    int --> float'''
    soma = 0
    for n in range(1,(N+1)):
        soma = soma + (1/n)
    return round(soma,3)