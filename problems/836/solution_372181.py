def busca(setor,matriz):
    """Funçao que recebe uma matriz com os dados de funcionarios de certa empresa 
    e  uma string indicando um setor da empresa, retorna os dados de todos os funcionarios que trabalham neste setor;
    str,list-->list"""
    lista = []
    matrizes = range(len(matriz))
    for i in matrizes:
        if setor == matriz[i][2]:
            lista = lista + [[matriz[i][0], matriz[i][1], matriz[i][3]]]
    return lista