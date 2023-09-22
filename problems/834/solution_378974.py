def media_matriz(Matriz):
    """Função que ao receber uma matriz, calcula e retorna a média de todos os
    números que a compõem com 2 casas decimais de precisão.
    list -> float"""
    soma=0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
                soma+=Matriz[i][j]
    return round((soma/(len(Matriz)/len(Matriz[0]))),2)