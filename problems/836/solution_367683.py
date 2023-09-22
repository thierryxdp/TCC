def busca(area,matriz):
    """A função recebe como entrada uma area da empresa e uma matriz,
    e retorna as informações pertencentes dos funcionários da area
    de entrada;
    str, list(list) -> list(list)"""
    soma_lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if str.upper(area) in str.upper(matriz[i][2]):
                list.pop(matriz[i],2)
                list.append(soma_lista, matriz[i])
    return soma_lista