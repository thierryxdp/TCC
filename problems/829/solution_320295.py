def soma_h (N):
    '''Função calcula a expressão H = 1 + 1/2 + 1/3  + (...) + 1/N). Sendo N um número inteiro.
    int - > float'''
    numero = 1
    for i in range (1,N):
        numero = numero + 1/i
    return round (numero,2)