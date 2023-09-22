def soma_h(n):
    '''retorna o valor da soma de "n" termos de "H"'''
    resultado = 1
    numerador = 1
    denominador = 1
    i=0
    while i < n:
        denominador += 1        
        s = numerador / denominador
        resultado = resultado + s
    return round(resultado,2)