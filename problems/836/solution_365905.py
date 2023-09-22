def busca(setor,dados):
    """ Função busca nos dados e retorna os funcionários que atuam no setor
        dado;
        str,list->list
        Parâmetros:
        setor: setor de atuação
        dados: matriz com o nome, registro, setor e telefone de cada funcionário
    """
    funcionarios=[]
    for i in range(len(dados)):
        if setor in dados[i][2]:
            list.append(funcionarios,dados[i])
    return funcionarios