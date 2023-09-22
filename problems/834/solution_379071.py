def media_matriz(m):
    '''Funcao recebe uma matriznao fazia e retorna e media da soma de todos os elementos da matriz
list -> flot'''
    acumulador = 0
    divisor = 0
    for i in m:
        for b in i:
            divisor += 1
            acumulador += b
    return round(acumulador/divisor,2)