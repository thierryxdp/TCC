def media_matriz(matriz):
    """Funcao que dada uma matriz de inteiros não vazia, retorna a media de todos os numeros da matriz(com exatamente duas casa decimais de precisao).
    list -> float"""
    soma_e = 0
    qtd_e = 0
    for linha in matriz:
        for elemento in linha:
            soma_e += elemento
            qtd_e += 1
    return round((soma_e/qtd_e),2)