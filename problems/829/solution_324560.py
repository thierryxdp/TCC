def soma_h(n):
    '''Função que recebe um número n e retorna o valor H com N (valor
    de entrada) termos
    
    int->float'''
    
    h = 0
    denominador = 0
    
    for contador in range(n):
        numerador = 1
        denominador = denominador + 1
        h = h + (numerador/denominador)
        
    return round(h,2)