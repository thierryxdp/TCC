def media_matriz(matriz):
    """Recebe uma matriz e retorna a média de todos os números dela, 
    com duas casas decimais de precisão.
    assinatura: list --> float
    testes:
    media_matriz([[1,1,1], [2,2,2], [3,3,0]]) == 1.67
    media_matriz([[1,1,1], [2,2,2]]) == 1.5
    """
    soma = 0
    qtdeElem = len(matriz)*len(matriz[0])
    for elementos in matriz:
        soma += sum(elementos)
    media = (soma)/(qtdeElem)
    return round(media,2)