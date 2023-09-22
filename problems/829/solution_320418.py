def soma_h(n):
    '''dada a equacao, returna a soma h de uma quantidade n de termos;
    int-> float'''
    soma = 0
    for x in range (1, n+1):
        soma = soma + (1/x)
    return round(soma,2)