def conta_numero(numero, matriz):
    
    ocorrencias = 0
    for indice1 in range(len(matriz)):
        
        pivo = int(indice1)
        for indice2 in matriz(pivo):
            if indice2 == numero:
                ocorrencias += 1
            
            else:
                pass
   	
    return ocorrencias