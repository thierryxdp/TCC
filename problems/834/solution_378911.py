def media_matriz(matriz):
    #Funcao que dada uma matriz de interios retorna a media de todos os numeros da matriz
    soma = 0
    for linha in matriz:
        for item in linha:
            soma += item
    media = soma/(len (matriz) * len (matriz[0]))
    media_arredondada = round(media,2)
    return media_arredondada