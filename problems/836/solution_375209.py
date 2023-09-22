def busca(setor,matriz):
    """retorna os dados de todos os funcionarios
    dado o nome de um setor da empresa e uma matriz
    com todas as informacoes.
    str, list -> list"""
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor.lower() == matriz[i][j].lower():
                infos = matriz[i].copy()
                infos.pop(infos.index(infos[j]))
                lista.append(infos)
    return lista