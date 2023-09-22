def melhor_volta(matriz):
    """Essa função retorna uma tupla com o melhor corredor, o seu melhor tempo
    e o número da volta com o melhor tempo. Como entrada uma lista e como saída
    uma tupla com todas as informações;
    list->tuple"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tempo=min(matriz[i])
    return(i,tempo,j)