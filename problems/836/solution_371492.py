def busca(setor,matriz):
    """recebe dados de funcionários da empresa na matriz, retorna os 
    dados dos funcionários do setor dado na entrada.
    str,list->list"""
    dados=[]
    for linha in matriz:
        if linha[2]==setor:
            linha.remove(setor)
            dados.append(linha)
    return dados