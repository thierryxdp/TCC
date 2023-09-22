def media_matriz (matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz com precisão de 2 casas decimais;
    list -> float'''
    soma_e = 0
    qtd_e = 0
    for linha in matriz:
        for elemento in linha:
            soma_e += elemento
            qtd_e += 1
    return round((soma_e/qtd_e),2)