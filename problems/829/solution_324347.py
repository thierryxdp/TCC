def soma_h(N):
    '''função que calcula e retorna o valor de H co (N) termos
    onde (N) é inteiro, a função deve retornar o resultado
    somente com 2 casas decimais; int -> float'''
    soma = 0
    for i in range(1, N + 1):
        H = (1/i)
        soma = soma + H
    return round(soma, 2)