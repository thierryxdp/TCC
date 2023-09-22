def soma_h(n):
    ''' funcao que dado um numero inteiro n retorna o valor h com n termos
    int->int'''
    soma = 0
    for i in range(1, n+1):
        soma = soma + 1/i
    return round(soma,2)