def media_matriz(matriz: list) -> float:
    """Retorna a média de todos os números da matriz 
    (com exatamente duas casas decimais de precisão)"""
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(lista,matriz[i][j])
    return round(sum(lista)/len(lista), 2)