def media_matriz(matriz):
    """retorna a média de todos os números da matriz.
    list->float"""
    soma=0
    qntd_valores=0
    media=soma/qntd_valores
    for linha in matriz:
        for valor in linha:
            soma=soma+linha[valor]
        qntd_valores=qntd_valores+1
    return media