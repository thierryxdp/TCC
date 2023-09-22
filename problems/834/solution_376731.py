def media_matriz(matriz):
    
    soma = 0
    qtd = 0
    for indice1 in range(len(matriz)):
        
        for indice2 in matriz[indice1]:
            soma += indice2
            qtd += 1
   	
    resultado = round((soma / qtd), 2)
    return resultado