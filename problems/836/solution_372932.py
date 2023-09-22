def busca(setor,matriz):
    """função que recebe matriz como entrada e faz uma busca na mesma e retorna seus dados; matriz-->lista"""
    lista = []
    for s in range(len(matriz)):
        if setor == matriz[s][2]:
            list.remove(matriz[s],setor)
            lista = lista + [matriz[s]]
    return lista