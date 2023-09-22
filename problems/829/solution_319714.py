# Soma H
def soma_h(n):
    '''Essa função recebe um número inteiro e retorna a soma da sequência
    1/n com n pertencente ao intervalo [1,n];
    INT -> FLOAT/INT'''
    soma = 0
    for i in range(1,n+1):
        soma += 1/i
    return round(soma,2)