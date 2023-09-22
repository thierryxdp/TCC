def busca(setor, matriz):
    """Dada uma matriz com os dados de funcionários de uma 
empresa e um setor, retorna os dados dos funcionáriso que 
pertencem ao setor dado.
list, str -> list"""
    saida= []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            saida+= [matriz[i][0], matriz[i][1], matriz[i][3]]
    return saida