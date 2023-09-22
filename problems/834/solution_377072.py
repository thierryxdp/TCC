def media_matriz(matriz):
    '''Funcao que retorna a media de todos os elementos da Matriz''' 
    tamanho = 0
    soma = 0

    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)

    return soma / tamanho