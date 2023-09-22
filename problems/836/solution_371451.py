def busca(setor,matriz):
    """Dado o setor de uma empresa e uma matriz contendo as informações dos funcionários,
    retorna os dados dos funcionários do setor pesquisado:
    list([Nome,Código,Setor,Telefone],...)-->list"""
    linha_matriz=len(matriz)
    coluna_matriz=len(matriz[0])
    resultado_da_busca=[]
    for i in range(linha_matriz):
        for j in range(coluna_matriz):
            if ((matriz[i][j].lower())==setor.lower()):
                resultado_da_busca+=[matriz[i]]
    return resultado_da_busca