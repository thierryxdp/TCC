def media_matriz(matriz):
    """retorna a média de todos os números da matriz.
    list->float"""
    soma=0
    qtd_elem=0
    for linha in matriz:
        for i in linha:
            soma=soma+linha[i]
        qntd_elem=qntd_elem+1
            return soma/qntd_elem