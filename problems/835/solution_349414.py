def melhor_volta(matriz):
    ''' 
    funcao criada para retornar uma tupla informando de quem e qual foi a melhor volta
    da prova
    parametros:
    matriz: matriz 6x10
    saida:
    inf sobre a melhor volta
    '''
    menos = []
    for i in range(len(matriz)):
        menos.append(min(matriz[i]))
        menor = min(menos)
    
    if menor in matriz[i]:
        quem = matriz.index(matrix[i])+1
        qual = matriz[i].index(min(menos))+1
        
    return (quem, menor, qual)