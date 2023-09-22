def conta_numero(numero,matriz):
    quant = 0
    
    for i in matriz:
        for j in i:
            if numero == j:
                quant += 1
        
    return quant