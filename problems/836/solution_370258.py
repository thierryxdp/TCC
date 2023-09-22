def busca(setor,matriz):
    """busca os dados dos funcionários de um determinado setor
    da empresa. str,matriz-->matriz"""
    quantidade=len(matriz)
    dados=[]
    for componentes in range(quantidade):
        if setor in matriz[componentes]:
            lista.append(matriz[componentes])
            matriz[componentes].remove(setor)
    return dados