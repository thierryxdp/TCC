def busca(setor, matriz):
    
    numTotalLinhas = len(matriz)
    linha = 0
    saida = []
    matriz2 = []
    numLinha = 0
    
    for lista in matriz:
        temp = []
        if lista[2] == setor:
            temp = lista
            del temp[2]
            matriz2.append(temp)
            
 

    return matriz2