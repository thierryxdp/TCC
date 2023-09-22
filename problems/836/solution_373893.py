def busca(setor ,matriz):
    """Funcao que dada uma matriz contendo informaçoes de cada funcionario
    como o nomer registro setor telefone e um setor faz uma busca por setor
    str, list --> list"""
    funcionarios = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i], setor)
            funcionarios = funcionarios + matriz[i]
    return funcionarios