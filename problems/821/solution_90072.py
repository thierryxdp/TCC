def fatorial(numero):
    'dado um numero retorne o calculo do fatorial deste numero.int-->int'
    calculo=1
    contador=1
    while contador<=numero:
        calculo=calculo*contador
        contador=contador+1
    return calculo