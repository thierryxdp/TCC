def busca(string, matriz):
    """essa função recebe uma string correspondendo a um
    setor de uma empresa e uma matriz com os dados de 
    funcionários de diferentes setores, e retorna apenas os 
    dados de quem for do setor solicitado;
    str,list-->list"""
    cont = []
    a = len(matriz)
    b = len(matriz[0])
    for i in range(a):
        for j in range(b):
            if string in matriz[i][2]:
                del(matriz[i][2])
                cont += [matriz[i]]
                if string in matriz[j][2]:
                    del(matriz[j][2])
                    cont += [matriz[i][j]]
    return cont