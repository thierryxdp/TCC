def busca(setor, relacaoFuncionarios):
    """
    Função que vasculha todos os funcionários de um determinado setor em uma empresa
    list -> list
    """

    i = 0
    funcionarios = []
    x = setor
    
    for i in range(len(relacaoFuncionarios)):
        if x == relacaoFuncionarios[i][2]:
            funcionarios.append(relacaoFuncionarios[i])
    
    if funcionarios != []:
        for j in range(len(funcionarios)):
            funcionarios[j].remove(x)

    
    return funcionarios