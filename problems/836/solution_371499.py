def busca(setor,matriz):
    """Dado o setor de uma empresa e uma matriz contendo as informações dos funcionários,
    retorna os dados dos funcionários do setor pesquisado:
    list([Nome,Código,Setor,Telefone],...)-->list"""
    linha_matriz=len(matriz)
    coluna_matriz=len(matriz[0])
    matriz_busca=[]
    resultado_da_busca=[]
    for i in range(0,linha_matriz):
        for j in range(0,coluna_matriz):
            print(matriz[i])
            if ((matriz[i][j].lower())==setor.lower()):
                resultado_da_busca+=[matriz[i]]
    return resultado_da_busca.remove(setor)