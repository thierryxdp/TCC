def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média
de todos os números da matriz (com exatamente duas casas decimais de precisão);
       mat --> float'''
    soma_colunas = [sum(x) for x in zip(*matriz)]
    numero_elementos = len(matriz) * len(matriz[0])
    media = (sum(soma_colunas))/numero_elementos
    return round(media,2)