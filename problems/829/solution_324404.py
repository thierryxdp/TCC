def soma_h(N):
    '''Calcula a soma de N termos no formato 1/N, aproximado para duas casas decimais, int->float'''
    soma = 0
    for elemento in range(N):
        soma = soma + 1/N
    return round(soma, 2)