def busca(setor, matriz):
    """Recebe uma matriz e faz uma busca por setor, dado um nome de um setor da empresa da matriz, retorna os dados de todos os funcionários
    str, list(lists) -> list(lists)"""
    y = []
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i, j)
                list.append(y, i)      
    return y