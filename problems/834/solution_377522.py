def media_matriz(matriz):
    '''Função que receba como entrada uma matriz de inteiros
    	não vazia, e retorne a média de todos os números da 
        matriz, com apenas duas casas decimais. 
        list --> float.'''
    media = 0 
    tamanho = 0
    for linha in matriz:
        media+=count.linha
        tamanho+=len(linha)
    return round(media/tamanho,2)