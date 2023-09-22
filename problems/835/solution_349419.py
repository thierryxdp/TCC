def melhor_volta(matriz):
    ''' 
    funcao criada para retornar uma tupla informando informacoes sobre a melhor volta
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
        q = matriz.index(matriz[i])+1
        qual = matriz[i].index(min(menos))+1
        
    return (q, menor, qual)