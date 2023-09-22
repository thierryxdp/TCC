def media(matriz):
    '''Função que retorna a media de todos os numeros da matriz
    list -> int '''
    soma = 0
    tamanho = 0

    for linha in matriz:
     soma += sum(linha)
     tamanho += len(linha)

    return soma / tamanho