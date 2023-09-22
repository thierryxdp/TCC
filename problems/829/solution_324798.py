def soma_h(N):
    '''A função calcula o valor H de uma soma de
    N termos onde cada fração tem o denominador 
    igual a sua posição na soma.
    int --> float'''

    soma = 0
    counter = 0
    limit = N + 1

    while counter < limit:
        if counter > 0:
            soma += 1 / counter
        counter += 1

    return round(soma, 2)