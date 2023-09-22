def media_matriz(m):
    '''Função que dada uma matriz de inteiros m, retorna a média de todos os números com 2 casas decimais de precisão
    list[list] -> float'''
    soma=0
    qtd=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma+=m[i][j]
            qtd+=1
    media=soma/qtd
    return round(media,2)