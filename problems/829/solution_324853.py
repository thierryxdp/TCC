def soma_h(numero):
    resultado = 0 
    
    for i in range(0,numero+1):
        resultado = resultado + 1/i
        
    return round(resultado,2)