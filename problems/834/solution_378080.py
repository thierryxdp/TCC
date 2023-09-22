def media_matriz(matriz):
    ''' função que dado uma matriz de inteiros não vazia, retorna 
    a média de todos os números da matriz (com exatamente duas casas
    decimais de precisão). list -> float'''
    soma, numeros = 0,0
    for a in range (len(matriz)):
        for b in range (len(matriz[a])):
            soma = soma + matriz[a][b]
            numeros = numeros + 1
        media = soma / numeros
        return round(media,2)