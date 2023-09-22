import math
def soma_h(N):
    '''Retorna o valor de 'h' , segundo o parametro de entrada 'N'
       int -> float'''
    h = round(0,2)
    for valor in range(N+1):
        if valor != 0:
            h += 1/(valor)
    return round(h,2)