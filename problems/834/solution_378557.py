def media_matriz(matriz):
    '''Função que retorna a média de 
    uma matriz
    list -> float'''
    dibisor = len(matriz) * len(matriz[0])
    somei = 0
    
    for linha in range(len(matriz)):
        
        for indice in range(len(matriz[linha])):
            somei = somei + matriz[linha][indice]
            
    dibidi = somei/dibisor
    arredundei = round(dibidi, 2)
    return arredundei