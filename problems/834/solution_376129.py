def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média
       de todos os números da matriz(com exatamente duas casas decimais precisão)
       matriz(int) ---> média(matriz)'''
    soma = 0.0
    media = 1
    nota = 1
    for i in range(matriz):
        soma = soma + nota
    media = soma / nota
    return media