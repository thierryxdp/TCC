def media_matriz (M): 
    '''Função que dada uma matriz de inteiros não vazia, retorna a média de todos 
    os números da matriz com duas casas decimais de precisão
    list -> tuple'''
    soma = 0
    tamanho = 0
    for linha in M:
        soma += sum(linha)
        tamanho += len(linha)
        media = soma/tamanho
    return round(media, 2)