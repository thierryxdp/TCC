def soma_h(n):
    ''' ... '''
    resultado = 1
    numerador = 1
    denominador = 1
    for i in range (0, n):
        denominador += 2

        numerador = numerador * -1

        s = numerador / denominador
        resultado = resultado + s

    return round(resultado, 2)