def soma_h(x):
    '''função que dado um numero como entrada, retorna o calculo da soma dos termos'''
    acumulador = 0
    for numero in range(1, x + 1):
        acumulador += (1 / numero)
    return round(acumulador ,2)