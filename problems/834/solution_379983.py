def media_matriz(matriz):
    """Funcao que dada uma matriz int nao vazia retorna a media de
    todos os numeros da matriz com duas casas decimais de precisao
    list --> float"""
    soma = 0
    qtd_numero = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            qtd_numero = qtd_numero + 1
    media = round(soma/qtd_numero, 2)
    return media