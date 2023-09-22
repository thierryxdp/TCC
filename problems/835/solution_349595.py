def melhor_volta(matriz):
    
    resultado_final = []
    
    for i in range(len(matriz)):
        
        for j in range(len(matriz[0])):
            
            resultado_final.append(matriz[i][j])
            
            min(resultado_final)
            tempo = min(resultado_final)
            
    return i+1, tempo, j+1