def media_matriz(matriz):
    '''função que dada uma matriz retorna a média dos números contidos na mesma em formato decimal com duas casas de precisão
    list-->float'''
    soma=0
    itens=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+(matriz[i][j])
            itens=itens+1
    media=soma/itens
    return round(media,2)