def busca(setor,matriz):
    """Essa funcao recebe uma matriz e um setor de uma empresa e retorna os contatos na matriz que participam deste setor
    str , list -> list"""
    resultado_busca = []
    for i in range (len(matriz)):
        if setor in matriz[i]:
            matriz[i].pop(setor)
            resultado_busca.append(matriz[i])
    return resultado_busca