def soma_h(n):
    """Uma função que calcule a soma de H, e retorne o valor
    de H com N termos; int=>float"""
    soma = 0
    for x in range(1, n + 1):
        R =  1/x
        soma = soma + R
    return round(soma,2)