def media_matriz(matriz):
    """Funcao que dada uma matriz de inteiros nao vazia, retorna a media de
    todos os numeros da matriz."""
    soma = 0
    qtd = 0

    #Percorrendo a linha
    for i in matriz:
        #Percorrer a colunas
        for j in i:
            soma = soma + j
            qtd += 1      

    media = soma/qtd
    return round(media,2)