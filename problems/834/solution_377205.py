def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    quantos_elementos = linhas*colunas
    soma = 0
    
     
    for i in range(linhas):
        for j in range(colunas): 
            soma += int(matriz[i][j])
            
    media = soma/quantos_elementos
           
    return round(media,2)