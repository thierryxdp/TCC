def soma_h(n):
    '''retorna o valor da soma de "n" termos de "H"'''
    resultado = 1
    numerador = 1
    denominador = 1
    for i in range(n):
        denominador += 1        
        s = numerador / denominador
        resultado = resultado + round(s,3)
    return round(resultado,2)