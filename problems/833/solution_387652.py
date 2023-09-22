def conta_numero(numero, matriz):
    
    conta=0
    
    for i in matriz:
        for j in matriz:
            if j == numero:
                conta += 1
                
    return conta