def media_matriz(matriz):
    """Função que dada a matriz da entrada retorna a media de todos os numeros da matriz; int-> float"""
    
    somatorio = 0
    ocorrencias = 0
    
    for indice in matriz:
        somatorio += sum(i)
        ocorrencias += len(indice)
        
    return round((somatorio/ocorrencias),2)