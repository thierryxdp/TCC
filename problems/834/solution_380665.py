def media_matriz:
    "funcao que tendo uma matriz de inteiros nao vazia, retorna a media de todos os numeros a matriz com ua casas decimais"
    media = 0
    soma = 0
    for linha in matriz:
        soma += sum(linha)
        meia = (soma/len(linha))len(matriz)
    return round(media,2)