def soma_h (N):
    '''Dada a função, calcule e retorne o valor de H com N
       termos onde N é inteiro;
       int -> float'''
    soma = 0
    for i in list(range(1, N+10):
        soma = soma + (1/i)
    return round(soma,2)