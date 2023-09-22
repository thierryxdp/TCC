def soma_h(n):
    """ função que dado um numero n, retorna o valor da soma H;
    int -> float"""
    soma = 0
    for elemento in range(1, n + 1):
        var1 = 1/elemento
        soma = soma + var1
    return round(soma,2)