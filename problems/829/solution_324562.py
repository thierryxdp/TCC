def soma_h(n):
    '''retorna o valor h com n termos, sendo n inteiro
    e dado de entrada
    int -> float'''
    soma = 0
    for x in range(1, n + 1):
        inversao = (1/x)
        soma += inversao
    return round(soma, 2)