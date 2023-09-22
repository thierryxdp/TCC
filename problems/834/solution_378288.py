def media_matriz(matriz):
    '''Função que, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz, com duas casas decimais de precisão.
list(list) --> float'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    lista_elementos = []
    for x in range(linhas):
        for y in range(colunas):
            soma = soma + matriz[x][y]
            lista_elementos = lista_elementos + [matriz[x][y]]
    media = soma/len(lista_elementos)
    return round(media,2)