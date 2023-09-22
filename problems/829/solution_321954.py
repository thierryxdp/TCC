def soma_h(n):
    
    i = 0
    resultado = 0
    for num in range(n):
        i = i+1
        resultado = resultado + (1/i)
        
    return round(resultado, 2)