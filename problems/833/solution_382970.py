def conta_numero(numero, matriz):
    
    ocorrencias = 0
    for indice1 in range(len(matriz)):
        
        for indice2 in matriz(indice1):
            if indice2 == numero:
                ocorrencias += 1
            
            else:
                pass
   	
    return ocorrencias