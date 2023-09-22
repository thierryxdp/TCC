def soma_h(n):
    ''' funcao que dada um numero inteiro ele calcula a soma dele com n termos'''
    soma = 0 
    for i in range(1, n+1):
        soma = (1/i) + soma
    return round(soma, 2)