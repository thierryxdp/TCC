def soma_h(n):
    resultado = 0
    count = 0
    for numero in range(n):
         count = count+1
        resultado = resultado + (1/count)
        
    return round(resultado,2)