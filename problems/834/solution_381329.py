def media_matriz(matriz):
    """Recebe uma matriz de inteiros não vazia e retorna a media de todos os numeros da matriz
    com duas casas decimais de precisão"""
    quantidade = 0
    soma = 0

    for conjunto in matriz:
        for unidade in conjunto:
            soma = soma + unidade
            quantidade = quantidade + 1
        
    media = soma / quantidade
    
    return round(media,2)