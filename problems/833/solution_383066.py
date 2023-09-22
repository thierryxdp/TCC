def conta_numero(numero, matriz):
    matriz = 0
    count = 0
    
    for x in matriz:
        if x == numero:
            count = count + 1
        
    return count