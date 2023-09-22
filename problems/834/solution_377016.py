def media_matriz(matriz):

    """ Função que dada uma matriz de inteiros não vazios, retorna a média de todos os números da matriz.
    A função retorna o seu resultado com apenas duas casas decimais."""
    
    soma = 0
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
          soma += matriz[i][j]
          contador += 1
    media = soma / contador
    return round(media, 2)