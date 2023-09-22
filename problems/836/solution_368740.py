def busca(matriz, setor):
    """Função que buscar os dados dos funcionários
    que pertencem ao setor pesquisado
    list, str -> list"""
    func = []
    for i in matriz:
        if i[2] == setor:
            func.append(i)
    return func