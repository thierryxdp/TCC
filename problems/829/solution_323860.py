def soma_h(N):
    ''' calcula e retorna o valor de H sendo N um inteiro qualquer dado
    como entrada 
    int --> float '''
    
    resultado = 1
    numerador = 1
    denominador = 1
    
    for i in range(N):
        denominador += 1
        
        
        s = numerador / denominador
        resultado = resultado + s
        
    return round(resultado, 2)