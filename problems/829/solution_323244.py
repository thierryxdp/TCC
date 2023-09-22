def soma_h(n):
    ''' Dado um número n qualquer, retorna
    o valor da soma H, até o termo n.
    int -> float'''
    soma = 0
    for i in range(n):
        soma += 1 + 1/i
    return round(soma,2)