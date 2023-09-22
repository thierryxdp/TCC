def soma_h(num):
    """ Funcao que recebe um numero inteiro "num" de entrada
    e retorna o valor H, dado pela formula "H=1+ 1/2 +1/3 +...+1/num" """
    """ int -> float """
    contador = 0
    for a in range(1, num + 1):
        H = 1 / a
        contador += H
    return round(contador, 2)
# Casos de teste:
""" soma_h(2)
>>> 1.5
    soma_h(3)
>>> 1.83
    soma_h(50)
>>> 4.5 """