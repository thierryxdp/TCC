def soma_h(n):
    '''Dado um numero n, retorna o somatorio de 1/n de 0 ate n
    int -> int'''
    serie = 0

    for i in range(n):
        serie += 1/(i+1)
    return round(serie,2)