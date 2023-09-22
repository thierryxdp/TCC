def busca(setor,matriz):
    """
    Retorna os dados de todos os funcionários do setor.
    str,list -> list
    """
    funcionarios=[]
    for i in range(len(matriz)):
        if m[i][2] == setor:
            list.remove(matriz, setor)
            funcionarios += m[i]
    return funcionarios