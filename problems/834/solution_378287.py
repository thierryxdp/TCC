def media_matriz(matriz):
    soma=0
    tamanho=0
    for linha in matriz:
        soma+=sum(linha)
        tamanho+=len(linha)
    return round(soma/tamanho,2)
'''funcao que recebe uma matriz e calcula a media de todos os
seus elementos
list->float'''