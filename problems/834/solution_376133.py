def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média
       de todos os números da matriz(com exatamente duas casas decimais precisão)
       matriz(int) ---> média(matriz)'''
    soma = 0.0
    for i in range(len(matriz)):
        soma = soma + sum(matriz[i])
    media = soma / (len(matriz) * len(matriz[0]))
    return round(media,2)