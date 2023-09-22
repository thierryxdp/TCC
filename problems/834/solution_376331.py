def media_matriz (matriz):
    '''Função calcula a media de todos os numeros da matriz (com precisão de 2 casa decimais.
    list -> float'''
    dividendo = 0 
    divisor = 0 
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            dividendo = dividendo + matriz [i][j]
            divisor = divisor +1
    media = dividendo / divisor 
    return round (media,2)