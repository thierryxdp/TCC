def busca(setor,matriz):
    """
    Retorna os dados de todos os funcionários do setor.
    str,list -> list
    """
    funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            del matriz[i][2]
            funcionarios += matriz[i]
    return funcionarios