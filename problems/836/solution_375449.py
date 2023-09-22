def busca(setor,matriz):
    """Essa funcao recebe uma matriz e um setor de uma empresa e retorna os contatos na matriz que participam deste setor
    str , list -> list"""
    resultado = []
    for x in range (len(matriz)):
        if setor in matriz[x]:
            matriz[x].pop(2)
            resultado.append(matriz[x])
    return resultado