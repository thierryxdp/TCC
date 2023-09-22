def media_matriz(matriz):
    '''dada uma matriz de inteiros, retorna a media
    de todos os numeros da matriz;
    matriz->float'''
    soma=0
    linha = 0
    for i in matriz:
        soma = soma + sum(i)
        linha= linha + len(i)
    return round((soma / linha),2)