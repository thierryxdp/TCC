def melhor_volta(matriz):
    
    tupla = (0,float('inf'),0)
        
    for i in range(len(matriz)):
         for j in range(len(matriz[i])):
                 if matriz[i][j] < tupla[1]:
                        tupla = (i+1,matriz[i][j],j+1)
    
    return tupla