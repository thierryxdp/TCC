def fatorial(numero):
   '''dado um numero calcula o fatorial desse numero'''

b = 1
    while numero > 0:
        b = b*numero
        numero = numero-1
    return b