def media_matriz(matriz):
    '''Função que retorna a média da "matriz" de entrada: list -> float'''
    
    somatorio = 0
    ocorrencias = 0
    
    for indice in matriz:
        somatorio += sum(indice)
        ocorrencias += len(indice)
        
    return round((somatorio/ocorrencias),2)