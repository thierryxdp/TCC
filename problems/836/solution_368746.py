def busca(setor, matriz):
    """Função que buscar os dados dos funcionários
    que pertencem ao setor pesquisado
    list, str -> list"""
    func = []
    for i in matriz:
        if setor == i[2]:
            func.append(i)
    return func