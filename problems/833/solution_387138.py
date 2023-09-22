def conta_numero(numero, matriz):
    
    contador = 0
    
    if len(matriz) == 0:
        return contador
     
    elif len(matriz) !=0:
       
        for i in range(len(matriz)):
        
            for j in range(len(matriz[0])):
                
                candidato = matriz[i][j]
            
                if candidato == numero:
                    contador +=1
                
        return contador