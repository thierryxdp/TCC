def melhor_volta(matriz):
    '''Função que recebe de entrada uma matriz 6x10 com tempo em segundo
    de seis corredores em 10 voltas. Função retorna tupla com o melhor corredor
    dado o menor tempo e em qual volta'''
    minimo = matriz[0][0]
    corredor = "Corredor 1"
    volta = "Volta 1"

    
    for i in range(len(matriz)):
       
        if min(matriz[i]) < minimo:
            
            minimo = min(matriz[i])
            corredor = (i+1)
            volta = (matriz[i].index(minimo) + 1)
        
    
    return corredor, minimo, volta