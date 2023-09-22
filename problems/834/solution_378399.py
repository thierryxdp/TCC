def media_matriz(matriz):
    """retorna a média de todos os números da matriz.
    list->float"""
    soma=0
    qntd_valores=0
    for linha in matriz:
        for valor in linha:
            soma=soma+linha[valor]
        qntd_valores=qntd_valores+1
    media=soma/qntd_valores
    return round(media,2)