def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros nã ovazia, retorna a
    	média de todos os números da matriz com duas casas deciamais
        de precisão
        
        list(list) -> float'''
    
    soma = 0
    total = len(matriz)*len(matriz[0])
    for linha in matriz:
        for coluna in linha:
            soma = soma + coluna
    return round(soma/total,2)