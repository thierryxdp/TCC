def melhor_volta(matriz):
  
    contlinha = 0
    contcoluna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(listatotal,matriz[i][j])
            
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(listatotal):
                contlinha = contlinha + i
                contcoluna = contcoluna + j
                
    return (contlinha,contcoluna)