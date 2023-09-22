def busca(setor,matriz):
    """A função retorna os dados de todos os funcionários registrados num setor da empresa;
    str,list[list...]->list[list...]"""
    funcionarios=[]
    for i in range(len(matriz)):
        leitura=matriz[:]
        if matriz[i][2]==setor:
            del leitura[i][2]
            funcionarios=funcionarios+leitura[i]
    return funcionarios