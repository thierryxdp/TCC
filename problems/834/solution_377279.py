def media_matriz(matriz):
    '''dada uma matriz de inteiros não vazia, retorna a média de todos os elementos
    da matriz, com precisão de 2 casas decimais;
    list --> float'''
    elementos = []
    for linha in matriz:
        for aij in linha:
            list.append(elementos,aij)
    media = sum(elementos)/len(elementos)
    return round(media,2)