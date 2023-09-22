def busca(setor, matriz):
    """Função que buscar os dados dos funcionários
    que pertencem ao setor pesquisado
    list, str -> list"""
    func = []
    for i in matriz:
        if setor == i[2]:
            s = i[:]
            list.del(s, setor)
            func.append(s)
    return func