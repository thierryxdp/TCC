def media_matriz(matriz):
    """Função que dada uma matriz, retorna a média de todos os números da matriz com 
       precisão de duas casas decimais.
       list->float"""
    tamanho = 0
    soma = 0
    media = 0
    if matriz !=[]:
        for linha in range(0,len(matriz)):
            for coluna in range(0,len(matriz[linha])):
                tamanho = tamanho + 1
                soma = soma + matriz[linha][coluna]
                media = soma / tamanho
    return round(media,2)