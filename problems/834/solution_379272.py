def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média de 
    todos os números da matriz (com exatamente duas casas decimais de precisão).
    list->float
    '''
    media=0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            media+=matriz[x][y]
  	
    return round((media/(len(matriz)*len(matriz[0]))),2)