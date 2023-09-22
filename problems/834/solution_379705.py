def media_matriz(matriz):
    '''
    funcao que recebe uma matriz e calcula a sua media
    com duas casas decimais
    list -> float
    '''
    
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
        
    return round((soma/tamanho),2)