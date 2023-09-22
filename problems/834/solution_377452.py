def media_matriz(matriz):
    '''função que dada uma matriz de nao inteiros vazia, retorna a media de todos os numeros da matriz
    (matriz)=matriz
    saida = float'''
    s=0
    t=0
    for linha in matriz:
        s+=sum(linha)
        t+=len(linha)
    return round((s/t),2)