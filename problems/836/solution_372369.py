def busca(setor,matriz):
    """  """
    lista = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            lista = lista + [[matriz[i][0], matriz[i][1], matriz[i][3]]]
    return lista