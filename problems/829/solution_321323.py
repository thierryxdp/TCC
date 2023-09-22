def soma_h(n):
    '''Calcula a soma de n termos de h'''
    h = 1 * (1 - (3/2) ** n)/1 - 3/2
    return round(h,2)