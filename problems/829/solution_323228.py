def soma_h (n):
    '''Dada a função, calcule e retorne o valor de H com N
       termos onde N é inteiro;
       int -> float'''
    soma = 0
    for i in list(range(1,n+1):
        soma = soma + (1/i)
    return round(soma,2)