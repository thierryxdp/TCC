def soma_h(n):
    '''funcao que dado um numero inteiro n calcula a soma definida com n termos
    int -> float'''
    soma = 0
    for i in range(1, n+1):
        soma = (1/i) + soma
    return round(soma, 2)